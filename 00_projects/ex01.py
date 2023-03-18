'''
這是函式庫內建的範例:example.py
'''
# 載入庫
from blinker import Device, ButtonWidget, NumberWidget
# 設備密鑰
device = Device("e6a060349d52")

# 物件
button1 = device.addWidget(ButtonWidget('btn-k1'))
button2 = device.addWidget(ButtonWidget('btn-k2'))
number1 = device.addWidget(NumberWidget('num-k3'))

# 變數
num = 0

########
# 函數 #
########
# 回呼函數:button1
async def button1_callback(msg):
    # 全域計次變數
    global num
    # 調用函數時 +1
    num += 1
    # text 是 APP 中數字元件左下角的文本
    # value 會顯示在數字元件中央的文本
    # .update 更新
    await number1.text("計次").value(num).update()

# 回呼函數:button2
async def button2_callback(msg):
    # {0} 回傳元件的「組件鍵名」
    # msg 就是動作屬性：tap、press、pressup
    print("Button2: {0}".format(msg))

# 系統函數-1
async def heartbeat_func(msg):
    print("--- 調用 heartbeat_func ---")
    print("Heartbeat func received: {0}".format(msg))
    # 文本组件

# 系統函數-2
async def ready_func():
    # 获取设备配置信息
    print("--- 調用 ready_func ---")
    print(vars(device.config))


# 設定回呼函數
button1.func = button1_callback
button2.func = button2_callback

# 這兩個函數會自動調用，目前我還不是很確定如何應用，但不可以缺少
device.heartbeat_callable = heartbeat_func
device.ready_callable = ready_func

# 主程式
if __name__ == '__main__':
    device.run()