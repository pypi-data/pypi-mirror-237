# Chainmaker-Python-SDK

[[长安链]](https://chainmaker.org.cn/)Python SDK。基于gRPC及[chainmaker/pb](https://git.chainmaker.org.cn/chainmaker/sdk-python)(protos)的链客户端。
提供链查询、链配置、用户合约管理、证书管理、公钥管理、订阅管理、多签管理、归档、Gas管理、交易池查询、DPos Erc20、DPos Stake、隐私计算等操作。

[sdk-python开源仓库地址](https://git.chainmaker.org.cn/chainmaker/sdk-python)

## 特性
- [x] 支持PermissionedWithCert、PermissionedWithKey、Public三种模式
- [x] 支持链查询,查询区块信息、区块头、区块高度、交易信息等
- [x] 支持查询链配置,更新核心配置、区块配置,增加修改删除信任根证书,增加修改共识节点等
- [x] 支持用户合约操作,合约查询、创建、更新、调用、查询、冻结、解冻、吊销等
- [x] 支持证书管理、证书哈希、证书别名管理及公钥管理
- [x] 支持Gas管理,查询设置Gas管理员,查询Gas账户状态、余额,Gas充值、退款等操作
- [x] 支持DPos Erc20、DPos权益、DPos惩罚、DPos奖励等相关操作
- [x] 支持交易池状态查询
- [x] 支持区块订阅、交易合约及订阅合约事件
- [x] 支持多签请求、投票、查询等，支持多签手动运行及自动运行
- [x] 支持交易黑名单功能
- [x] 支持隐私计算
- [x] 支持国密非TLS场景(如,Public模式+国密)
- [x] 支持共识高度、共识状态等查询


## 安装方法

> chainmaker-python-sdk支持 python3.6~python3.10, 已知python3.11安装pysha3存在问题

**在线安装**

```shell
$ pip install chainmaker
```

## 使用方法

### 以配置文件形式创建ChainClient
> [配置文件sdk_config.yml格式参考](https://docs.chainmaker.org.cn/operation/配置文件一览.html#sdk-config-yml)


配置文件`./testdata/sdk_config.yml`参考内容
```yaml
chain_client:
  chain_id: "chain1"
  org_id: "wx-org1.chainmaker.org"
  user_key_file_path: "./testdata/crypto-config/wx-org1.chainmaker.org/user/client1/client1.tls.key"
  user_crt_file_path: "./testdata/crypto-config/wx-org1.chainmaker.org/user/client1/client1.tls.crt"
  user_sign_key_file_path: "./testdata/crypto-config/wx-org1.chainmaker.org/user/client1/client1.sign.key"
  user_sign_crt_file_path: "./testdata/crypto-config/wx-org1.chainmaker.org/user/client1/client1.sign.crt"

  nodes:
    - node_addr: "127.0.0.1:12301"  # 节点rpc服务地址
      enable_tls: true
      conn_cnt: 1
      trust_root_paths:
        - "./testdata/crypto-config/wx-org1.chainmaker.org/ca"
        - "./testdata/crypto-config/wx-org2.chainmaker.org/ca"
      tls_host_name: "chainmaker.org" 
```
> 注: sdk_config.yml中私钥/证书等如果使用相对路径应相对于当前运行起始目录,建议使用绝对路径

使用配置文件创建链客户端
```python
from chainmaker import ChainClient
# 创建链客户端
cc = ChainClient.from_conf('./testdata/sdk_config.yml')
# 获取链版本
print(cc.get_chainmaker_server_version())
```
> 使用管理台生成的链由于生成的证书未包含部署服务器的域名使用sdk-python可能导致连接不上，参见[已知问题](#已知问题)

### 以参数形式创建ChainClient

```python
from chainmaker import Node, User, ChainClient

crypto_config_path = './testdata/crypto-config'
node_addr = '127.0.0.1:12301'

def read_file_bytes(file_path):
    return open(file_path, 'rb').read()

# 创建签名用户
user = User(
    org_id='wx-org1.chainmaker.org',
    sign_key_bytes=read_file_bytes(f'{crypto_config_path}/wx-org1.chainmaker.org/user/client1/client1.tls.key'),
    sign_cert_bytes=read_file_bytes(f'{crypto_config_path}/wx-org1.chainmaker.org/user/client1/client1.tls.crt'),
    tls_key_bytes=read_file_bytes(f'{crypto_config_path}/wx-org1.chainmaker.org/user/client1/client1.sign.key'),
    tls_cert_bytes=read_file_bytes(f'{crypto_config_path}/wx-org1.chainmaker.org/user/client1/client1.sign.crt')
)

# 创建连接节点
node = Node(
    node_addr=node_addr,
    conn_cnt=1,
    enable_tls=True,
    trust_cas=[read_file_bytes(f'{crypto_config_path}/wx-org1.chainmaker.org/ca'),
               read_file_bytes(f'{crypto_config_path}/wx-org2.chainmaker.org/ca')],
    tls_host_name='chainmaker.org'
)

# 创建链客户端
cc = ChainClient(chain_id='chain1', user=user, nodes=[node])
# 获取链版本
print(cc.get_chainmaker_server_version())
```

### 创建wasm合约

```python

from chainmaker import ChainClient, RuntimeType

crypto_config_path = './testdata/crypto-config'

# 背书用户配置
endorsers_config = [
    {'org_id': 'wx-org1.chainmaker.org',
     'user_sign_crt_file_path': f'{crypto_config_path}/wx-org1.chainmaker.org/user/admin1/admin1.sign.crt',
     'user_sign_key_file_path': f'{crypto_config_path}/wx-org1.chainmaker.org/user/admin1/admin1.sign.key'},
    {'org_id': 'wx-org2.chainmaker.org',
     'user_sign_crt_file_path': f'{crypto_config_path}/wx-org2.chainmaker.org/user/admin1/admin1.sign.crt',
     'user_sign_key_file_path': f'{crypto_config_path}/wx-org2.chainmaker.org/user/admin1/admin1.sign.key'},
    {'org_id': 'wx-org3.chainmaker.org',
     'user_sign_crt_file_path': f'{crypto_config_path}/wx-org3.chainmaker.org/user/admin1/admin1.sign.crt',
     'user_sign_key_file_path': f'{crypto_config_path}/wx-org3.chainmaker.org/user/admin1/admin1.sign.key'},
]

cc = ChainClient.from_conf('./testdata/sdk_config.yml')


# 创建WASM合约，本地合约文件./testdata/contracts/rust-fact-2.0.0.wasm应存在
payload = cc.create_contract_create_payload(
    contract_name='fact', 
    version='1.0', 
    byte_code_or_file_path='./testdata/contracts/rust-fact-2.0.0.wasm',
    runtime_type=RuntimeType.WASMER, 
    params={})
# 创建背书
endorsers = cc.create_endorsers(payload, endorsers_config)
# 发送创建合约请求
tx_response = cc.send_contract_manage_request(payload, endorsers=endorsers, with_sync_result=True)
print(tx_response)
```
### 创建evm合约

```python
from chainmaker import ChainClient, RuntimeType

crypto_config_path = './testdata/crypto-config'

# 背书用户配置
endorsers_config = [
    {'org_id': 'wx-org1.chainmaker.org',
     'user_sign_crt_file_path': f'{crypto_config_path}/wx-org1.chainmaker.org/user/admin1/admin1.sign.crt',
     'user_sign_key_file_path': f'{crypto_config_path}/wx-org1.chainmaker.org/user/admin1/admin1.sign.key'},
    {'org_id': 'wx-org2.chainmaker.org',
     'user_sign_crt_file_path': f'{crypto_config_path}/wx-org2.chainmaker.org/user/admin1/admin1.sign.crt',
     'user_sign_key_file_path': f'{crypto_config_path}/wx-org2.chainmaker.org/user/admin1/admin1.sign.key'},
    {'org_id': 'wx-org3.chainmaker.org',
     'user_sign_crt_file_path': f'{crypto_config_path}/wx-org3.chainmaker.org/user/admin1/admin1.sign.crt',
     'user_sign_key_file_path': f'{crypto_config_path}/wx-org3.chainmaker.org/user/admin1/admin1.sign.key'},
]

cc = ChainClient.from_conf('./testdata/sdk_config.yml')
# 创建EVM合约，本地合约文件./testdata/contracts/ledger_balance.bin应存在
payload = cc.create_contract_create_payload(
    contract_name='balance001', 
    version='1.0', 
    byte_code_or_file_path='./testdata/contracts/ledger_balance.bin',
    runtime_type=RuntimeType.EVM)
# 创建背书
endorsers = cc.create_endorsers(payload, endorsers_config)
# 发送创建合约请求
tx_response = cc.send_contract_manage_request(payload, endorsers=endorsers, with_sync_result=True)
print(tx_response)
```

### 调用wasm合约

```python
from chainmaker.chain_client import ChainClient
from chainmaker.utils.evm_utils import calc_evm_method_params

# 创建客户端
cc = ChainClient.from_conf('./testdata/sdk_config.yml')

# 调用WASM合约
tx_response = cc.invoke_contract(
    contract_name='fact',
    method='save',
    params={"file_name": "name007", "file_hash": "ab3456df5799b87c77e7f88", "time": "6543234"},
    with_sync_result=True)

print(tx_response)
```

### 调用evm合约

```python
from chainmaker.chain_client import ChainClient
from chainmaker.utils.evm_utils import calc_evm_method_params

# 创建客户端
cc = ChainClient.from_conf('./testdata/sdk_config.yml')
# 调用EVM合约
evm_contract_name = 'balance001'  # EVM合约名不再需要进行转换
evm_method, evm_params = calc_evm_method_params(
    method='updateBalance', 
    params=[{"uint256": "10000"}, {"address": "0xa166c92f4c8118905ad984919dc683a7bdb295c1"}])

tx_response = cc.invoke_contract(
    contract_name=evm_contract_name, 
    method=evm_method, 
    params=evm_params, 
    with_sync_result=True)

print(tx_response)
```

### 更多示例和用法

> 更多示例和用法，请参考单元测试用例

| 功能    | 单测代码                            |
|-------|---------------------------------|
| 用户合约  | `tests/test_user_contract.py`   |
| 系统合约  | `tests/test_system_contract.py` |
| 链配置   | `tests/test_chain_config.py`    |
| 证书管理  | `tests/test_cert_manage.py`     |
| 消息订阅  | `tests/test_user_contract.py`   |


## 接口说明

详细参考: [SDK接口文档](SDK_INTERFACES.md)

## 变更纪录

详细参考[CHANGELOG](CHANGELOG.md)

## 如何运行测试


1. 安装测试需要的依赖
```shell
pip install -r requirements-test.txt
```
2. 下载并拷贝被测环境的crypto-config到tests/resources/目录下

3. 修改tests/resources/sdk_config.yml中的节点地址或修改tests/pytest.ini中是sdk_config配置指定sdk_config.yml路径

4. 运行测试
```shell
pytest tests
```

## 如何进行开发

1. 安装依赖
```shell
pip install requirements-dev
```

更新protos
```shell
make proto
```


测试覆盖率
```shell
make coverage
```

检查代码
```shell
make lint
```

发布
```shell
make release
```

## TODO
- [ ] 支持国密TLS
- [ ] 实现Hibe加密

## 已知问题
- [ ] 使用Python3.11安装时,pysha3会build失败，可以改为Python3.6～python3.10，建议使用Python3.9
- [ ] 使用管理台部署的链，使用sdk-python连接报错(使用sdk-go能连接)，可能原因为管理台生成的证书扩展SAN(SubjectAlternativeName)中不包含部署服务的域名导致OpenSSL验证失败所致(sdk-go不验证该项),可以尝试在sdk_config.yml的tls_host_name修改为你的域名,或尝试使用
[chainmaker-cryptogen](https://git.chainmaker.org.cn/chainmaker/chainmaker-cryptogen)项目生成证书。

## 参考

- [chainmaker-docs](https://docs.chainmaker.org.cn/index.html)
- [gRPC Python](https://grpc.github.io/grpc/python)
- [grpcio](https://grpc.io/docs/languages/python/quickstart/)
- [cryptography](https://cryptography.io/)
- [eth-abi](https://eth-abi.readthedocs.io/en/latest/)



