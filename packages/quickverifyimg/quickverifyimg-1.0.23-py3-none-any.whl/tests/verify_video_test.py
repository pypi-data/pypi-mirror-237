import os
import time

from quickverifyimg.log.logger import get_logger
from quickverifyimg.quick_verify import QuickVerify
from quickverifyimg.quick_verify_video import QuickVerifyVideo

logger = get_logger(__name__)

if __name__ == '__main__':
    """
    crop_place：{ size: 需要识别的区域的大小， 百分比, offset: 需要识别的区域的左上角坐标点位置， 百分比}
    quick_verify: 是否快速校验，即不对已校验过的对照集图片继续校验
    """
    # origin_video = "./images/video/iPhone14ProMax.mp4"
    # target_video = "./images/video/iPhoneSE3.mp4"
    target_video = os.path.join("images", "video", "target.mp4")
    origin_video = os.path.join("images", "video", "origin1697697743")
    back = os.path.join("images", "video", "back.png")
    # crop_place = {"size": (0.48, 0.95), "offset": (0.13, 0)}
    size = (0.42917, 1.0)
    offset = (0.18125, 0)
    crop_place = {"size": size, "offset": offset}  # {size: 需要识别的区域的大小， 百分比, offset: 需要识别的区域的左上角坐标点位置， 百分比}
    # 选择使用的图片匹配算法和阈值
    # ac_tpl：模版匹配：大图找小图，速度快推荐
    # hist: 直方图匹配：速度一般，效果
    # ssim: ssim匹配算法：精准，速度不快，适合作为第二个算法补充
    # psnr: 峰值信噪比算法：目前只判断40以上为匹配，即认为相似度0.999
    # hash_p: 感知哈希算法：速度快，效果一般
    # hash_a: 均值哈希算法：速度快，效果一般
    # hash_d: 查值哈希算法：速度快，效果一般
    verify_engine_list = [
        ('ac_tpl', 0.993),
        ('hist', 0.998)
    ]
    quick_v = QuickVerifyVideo(verify_engine_list, 0.8, crop_place=None, background_similar=0.99, auto_crop=True, background_path=back)
    ret = quick_v.verify_video_effect(None, target_video, origin_img_dir=origin_video)
    print(f"匹配结果：{ret['result']}")
    print(f"匹配失败图片：{ret['verify_fail_screenshots']}")
    print(f"整体成功率：{ret['final_match_rate']}")