#这个文件用于统一debug模式信息所使用
#基础组件
#维护停服模式检测
async def jc_fix():
    import xxt.setting as sz
    from lib.nblib.helpers import render_expression as expr
    import lib.nblib.smartlib as e
    if sz.FixMode ==True:
        return f'{expr(e.Maintenance_CHAT)}'