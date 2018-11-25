import itsdangerous


# TYPE: Third-party package

def _help():
    # 交互界面查看文档，使用help(),退出quit
    print(itsdangerous.__doc__)


def _signer():
    # 密钥签名
    s = itsdangerous.Signer('secret-key')
    i_str = s.sign("My name is zyp")
    print(s.unsign(i_str))


def _timestamp_signer():
    # 带时间戳的签名
    s = itsdangerous.TimestampSigner('secret-key')
    i_str = s.sign("My name is zyp")
    print(s.unsign(i_str))


def _serializer():
    # 序列化
    s = itsdangerous.Serializer('secret-key')
    s.loads(s.dumps([1, 2, 3]))


def _timed_serializer():
    # 带时间戳序列化
    s = itsdangerous.TimedSerializer('secret-key')
    s.loads(s.dumps([1, 2, 3]))


def _url_safe_serializer():
    # URL安全序列化
    s = itsdangerous.URLSafeSerializer('secret-key')
    s.loads(s.dumps([1, 2, 3]))


def _json_web_signature_serializer():
    # JSON Web签名(jwt)
    s = itsdangerous.JSONWebSignatureSerializer('secret-key')
    s.loads(s.dumps({'x': 42}))


def _timed_json_web_signature_serializer():
    # JSON Web签名(jwt)带时间戳
    s = itsdangerous.TimedJSONWebSignatureSerializer('secret-key')
    s.loads(s.dumps({'x': 42}))


if __name__ == "__main__":
    # _help()
    pass
