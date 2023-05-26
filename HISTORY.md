## v0.10.3 (2023-05-11)

### Feat

- k, ohlc 接口支持前复权功能

### Fix

- Python 版本支持 3.8 ~ 3.11
- 修正后复权功能, xdxr 进行缓存化加速

## v0.10.1 (2023-05-10)

### Feat

- holiday 添加缓存, 并增加测试代码
- 添加缓存模块, 并增加测试代码

### Fix

- js_decode 文件分离
- minute 接口数据异常修复, 使用 minutes 获取当天数据即可
- 修正读取通达信本地数据复权问题

## v0.10.0 (2023-05-09)

### Feat

- 移除非必要依赖

### Fix

- incon.dat 所处的位置错误
- 修正前复权计算错误问题