# ff14AutoChangePrice
ff14自动改价，模拟键盘输入。
- 100%模拟键盘操作，没有读取任何游戏数据。
- 【！！！注意！！！】需要结合卫月框架插件中官方仓库作者tesu的Penny Pincher插件。
  - 其作用为打开调整物品价格时价窗口时自动复制当前最低价格减1（可配置）。
  - [卫月框架](https://bbs.tggfl.com/topic/32/dalamud-%E5%8D%AB%E6%9C%88%E6%A1%86%E6%9E%B6。)
  - [PennyPincher插件](https://github.com/tesu/PennyPincher。)
- 【！！！注意！！！】由于需要使用win32api向游戏窗口发送键盘消息，需要以管理员模式运行。

拥有一键更改所有雇员价格和一键更改单个雇员内价格两种模式。
### 1模式需要手动进入雇员铃，输入雇员商品数量：
etc. 第一位雇员出售中5件商品，第二位雇员出售中3件商品，第三位雇员出售2件商品，输入就是“5 3 2”。
### 2模式用于快速清空背包发布销售：
可以无视价格在雇员界面上货时上一堆货然后用程序自动改价。
2模式新增仅更新指定商品的模式。![image](https://github.com/PinkYuDeer/ff14AutoChangePrice/assets/83949453/cdfd3302-3fbe-44a7-a270-2425cc5392dc)


