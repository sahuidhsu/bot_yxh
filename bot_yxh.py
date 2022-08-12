"""营销号生成
发送 yxh 主体 动作 原因
"""

from botoy import GroupMsg, S, decorators
from botoy.parser import group as gp
from botoy.sugar import Text

@decorators.ignore_botself
@decorators.startswith("yxh")
def receive_group_msg(ctx: GroupMsg):
    input_text = ctx.Content[3:]
    if not input_text:
        return
    
    items = [i.strip() for i in input_text.split(" ") if i]
    if items:
        if len(items) != 3:
            return
        else:
            result=f"{items[0]}{items[1]}是怎么回事呢？" \
                   f"{items[0]}相信大家都很熟悉，" \
                   f"但是{items[0]}{items[1]}是怎么回事呢，下面就让小编带大家一起了解吧。\n" \
                   f"{items[0]}{items[1]}，其实就是{items[2]}。" \
                   f"大家可能会很惊讶{items[0]}怎么会{items[1]}呢？但事实就是这样，" \
                   f"小编也感到非常惊讶。\n这就是关于{items[0]}{items[1]}的事情了，" \
                   f"大家有什么想法呢，欢迎在评论区告诉小编一起讨论哦！"
        Text(result)