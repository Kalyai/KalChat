from tortoise import Model, fields  # noqa


class AccountModel(Model):
    id = fields.IntField(pk=True)
    login = fields.CharField(64)
    password = fields.CharField(128)

    class Meta:
        schema = 'auth'
        table = 'accounts'
