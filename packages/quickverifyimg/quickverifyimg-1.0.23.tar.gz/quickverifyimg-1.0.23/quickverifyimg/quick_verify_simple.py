import math
import os
import traceback

import cv2
from natsort import ns, natsorted

import copy

from quickverifyimg.log.logger import get_logger
from quickverifyimg.utils.aircv_utils import match_image
from quickverifyimg.utils.cv2_utils import compare_hist, ssim, compare_hsv_h, compare_hsv_s, comparet_hsv_v, compare_hsv
from quickverifyimg.utils.hash_utils import getHash_similarity_p, getHash_similarity_d, getHash_similarity_a
from quickverifyimg.utils.image_utils import crop_frame
from quickverifyimg.utils.psnr import get_psnr_similar
from quickverifyimg.utils.thread_utils import MyThread
logger = get_logger(__name__)

switcher = {
    'ac_tpl': match_image,
    'hist': compare_hist,
    'cv_hsv_h': compare_hsv_h,
    'cv_hsv_s': compare_hsv_s,
    'cv_hsv_v': comparet_hsv_v,
    'cv_hsv': compare_hsv,
    'ssim': ssim,
    'psnr': get_psnr_similar,
    'hash_p': getHash_similarity_p,
    'hash_a': getHash_similarity_a,
    'hash_d': getHash_similarity_d,
}
"""
内存精简版
"""
class QuickVerifySimple():
    def __init__(self, verify_img_dir, backgroup_img_path, crop_place=None, quick_verify=False, background_num_after_start_max=30, background_similar=0.998):
        """
        :param verify_img_dir: 对照图片集文件路径
        :param backgroup_img_path: 背景图路径
        :param crop_place: 需要裁剪的位置： {"size": (0.815, 1.0), "offset": (0.175, 0)}  # 去掉顶部0.175位置
        :param quick_verify: 是否快速校验，即不对已校验过的对照集图片继续校验
        :param background_num_after_start_max: 特效开始后最大背景图数
        """
        self.quick_verify = quick_verify
        self.crop_place = crop_place
        self.verify_img_dir = verify_img_dir
        self.backgroup_img_path = backgroup_img_path
        self.background_num_after_start_max = background_num_after_start_max
        self.background_similar = background_similar
        self.backgroup_img = cv2.imread(self.backgroup_img_path)
        # 获取用来校验的图片集
        self.verify_images_file_list = os.listdir(self.verify_img_dir)
        self.verify_images_file_list = natsorted(self.verify_images_file_list,
                                            alg=ns.PATH)  # 要加alg=ns.PATH参数才和windows系统名称排序一致
        self.verify_images = []
        self.verify_images_name = []
        self.first_img_background = None
        for file_name in self.verify_images_file_list:
            file_path = os.path.join(verify_img_dir, file_name)
            # if not os.path.isfile(file_path):
            #     continue
            self.verify_images.append(file_path)
            self.verify_images_name.append(file_name)

            # 如果校验图片目录中没有图片，直接返回false
        if len(self.verify_images) < 1:
            logger.error(f"no image in verify_images_dir {verify_img_dir}")
            raise Exception("no image in verify_img_dir")

    def verify_img(self, img_list, verify_img_index, verify_engine_list=[('ac_tpl', 0.99)]):
        """
        检验图片
        :param verify_engine_list: 校验图片算法
        :param img_list: 待校验图片集
        :param verify_img_index: 对照图片集开始顺序
        :return:
        """
        is_start = False
        background_num_after_start = 0
        background_num_after_start_max = self.background_num_after_start_max
        cut_match_index = -1
        available_screenshot_num = 0  # 非背景图的截图的数量
        match_times = 0  # 跟verify_images_dir对比，相似度超过阈值的图片数量
        verify_fail_screenshots = []
        available_screenshot_list = []
        for img_path in img_list:
            img = cv2.imread(img_path)
            if self._similiar_with_background(img, self.backgroup_img, verify_engine_list):
                if not is_start:  # 特效未开始，但截图跟背景图一样，应该是截图早了，判断下一张即可
                    continue
                elif background_num_after_start > background_num_after_start_max:  # 特效已开始，而截图跟背景图一样，如果连续出现30次，认为是特效已经展示完了
                    logger.info(
                        f"background_num_after_start > {background_num_after_start_max}, break this verify {img_path}")
                    break
                else:
                    logger.info(f"found a background img with {img_path}")
                    background_num_after_start += 1  # 特效已开始，而截图跟背景图一样，未达到连续30次，只记录次数，说不定是特效效果就这样
                    continue
            else:
                available_screenshot_list.append(img_path)
                available_screenshot_num += 1
                background_num_after_start = 0  # 截图跟背景图不一样，刷新次数

            best_matching_name = ''
            best_matching_similar = 0
            best_matching_engine = ''
            verify_images = self.verify_images[verify_img_index:len(self.verify_images)]
            verify_images_name = self.verify_images_name[verify_img_index:len(self.verify_images_name)]
            tmp_verify_images = copy.deepcopy(verify_images)
            for index, verify_img in enumerate(verify_images):
                # 因为截图和校验图都是连续的，所以如果有校验通过了的校验图，下次校验时可以跳过此次之前的图片
                if self.quick_verify and index < cut_match_index:
                    continue
                verify_img = cv2.imread(verify_img)
                is_similar, similar, engine = self._is_image_similar(img, verify_img, verify_engine_list)
                if is_similar:
                    logger.info(f"{img_path} 比对 {verify_images_name[index]}, 相似度: {similar} , 算法 :{engine}")
                    if not self.quick_verify:
                        tmp_verify_images.pop(index)
                    cut_match_index = index
                    match_times += 1
                    is_start = True
                    best_matching_name = ""
                    break
                else:
                    if best_matching_similar < similar:
                        best_matching_similar = similar
                        best_matching_name = self.verify_images_name[index]
                        best_matching_engine = engine
            if best_matching_name:
                verify_fail_screenshots.append(img_path)
                logger.info(
                    f"{os.path.basename(img_path)} 匹配不上任何图片, threshold: {verify_engine_list}, "
                    f"相似度最高图片: {best_matching_name}"
                    f"相似度 : {best_matching_similar}"
                    f"匹配算法 :{best_matching_engine}"
                )
        return {
           'available_screenshot_num':available_screenshot_num,
           "match_times": match_times,
           "verify_fail_screenshots":verify_fail_screenshots,
            "available_screenshots":available_screenshot_list
        }

    def _similiar_with_background(self, img, background_image, verify_engine_list):
        """
        背景图要求相似度为0.998
        :param img:
        :param background_image:
        :param verify_engine_list:
        :return:
        """
        background_verify_engine_list = []
        for item in verify_engine_list:
            background_item = (item[0], self.background_similar)
            background_verify_engine_list.append(background_item)
        is_similar, _, engine = self._is_image_similar(img, background_image, background_verify_engine_list, is_background=True)
        if is_similar:
            return True
        else:
            # 增加环节，如何和第一张一样，也认为是背景图
            if self.first_img_background is not None:
                is_first_similar, _, engine = self._is_image_similar(img, self.first_img_background, background_verify_engine_list,
                                                               is_background=True)
                if is_first_similar:
                    return True
            return False

    def _is_image_similar(self, image1, image2, verify_engine_list, is_background=False):
        image1_crop = image1
        image2_crop = image2
        # crop_place = {"size": (0.815, 1.0), "offset": (0.175, 0)}
        if self.crop_place:
            image1_crop = crop_frame(image1, **self.crop_place)
            image2_crop = crop_frame(image2, **self.crop_place)
        best_similar = 0
        best_engine = ''
        for engine in verify_engine_list:
            get_similar = switcher.get(engine[0], "")
            similar = get_similar(image1_crop, image2_crop)
            if float(engine[1]) <= float(similar):
                return True, similar, engine[0]
            else:
                if best_similar < similar:
                    best_similar = similar
                    best_engine = engine[0]
        if is_background:
            logger.info(f"与背景图的相似度为：{similar}")
        return False, best_similar, best_engine


    def mutliple_engine_verify(self, img_dir, verify_engine_list, match_rate_threshold, offset_size=10):
        """
        多算法调用
        :param img_dir:
        :param verify_type_list: {(1, 0.99), (2, 0.98}
        :param match_rate_threshold:
        :param offset_size: 快速校验偏移量，
        :return:
        """
        img_list = []
        effect_screenshot = os.listdir(img_dir)
        effect_screenshot.sort(key=lambda x: int(x[:-4]) if x[:-4].isdigit() else x[:-4])  # 去掉后缀名来排序
        for file_name in effect_screenshot:
            file_path = os.path.join(img_dir, file_name)
            if not os.path.isfile(file_path):
                continue
            img_list.append(file_path)

        # 先查找特效的第一张图片
        start_index = 0
        first_img = cv2.imread(img_list[0])
        for img_path in img_list:
            img = cv2.imread(img_path)
            if self._similiar_with_background(img, first_img, verify_engine_list):
                start_index += 1
            else:
                break
        if start_index >= len(img_list):
            logger.error('均匹配为背景图，请检查匹配算法阈值')
            ret = {
                'final_match_rate': 0,
                'verify_fail_screenshots': [],
                'available_screenshot_num': 0,
                'available_screenshots': 0,
                'result': False
            }
            return ret
        self.first_img_background = first_img
        logger.info(f'特效开始的第一张图片：{img_list[start_index]}')
        img_list = img_list[start_index: len(img_list)]
        # 10张图片就开一个线程去查询
        img_threshold = 50
        thread_list = []
        available_screenshot_sum = 0
        match_times_sum = 0
        verify_fail_screenshots_all = []
        available_screenshot_list_all = []

        max_threads = 10  # 最大线程数
        if max_threads < math.ceil(len(img_list)/img_threshold):
            # 如果超过最大线程数，调整每个线程数处理的图片数量
            img_threshold = math.ceil(len(img_list)/max_threads)

        for i in range(0, len(img_list), img_threshold):
            all_list_temp = img_list[i:i + img_threshold]
            # 对照集的开始校验的图片序号
            verify_index = 0
            if self.quick_verify:
                # 如果是快速校验，则往前偏移指定量照片开始校验
                verify_index = i - offset_size
                if verify_index < 0:
                    verify_index = 0
            thread = MyThread(self.verify_img, args=(all_list_temp, verify_index),
                              kwargs={'verify_engine_list': verify_engine_list})
            thread.start()
            thread_list.append(thread)
        for t in thread_list:
            t.join()
            ret = t.get_result()
            try:
                available_screenshot_list_all.extend(ret["available_screenshots"])
                available_screenshot_sum += ret["available_screenshot_num"]
                match_times_sum += ret["match_times"]
                verify_fail_screenshots_all.extend(ret["verify_fail_screenshots"])
            except Exception as e:
                logger.error(f'线程收集数据异常:{e}')
                logger.error(traceback.format_exc())
                logger.error(f'result: {ret}')

        # 计算匹配率 (达到相似度阈值的截图数量 / 非背景图的截图数量)
        final_match_rate = 0
        if available_screenshot_sum:
            final_match_rate = match_times_sum / available_screenshot_sum
        ret = {
            'final_match_rate': final_match_rate,
            'verify_fail_screenshots': verify_fail_screenshots_all,
            'available_screenshot_num': available_screenshot_sum,
            'available_screenshots': available_screenshot_list_all
        }
        if final_match_rate >= match_rate_threshold:
            ret['result'] = True
        else:
            ret['result'] = False
        return ret