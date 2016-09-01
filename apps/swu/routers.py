class LogRouter(object):

    models = ['swu' + '.' + m for m in ['generallog', 'speciallog', 'signallog']]

    def db_for_read(self, model, **hints):
        if str(model._meta) in self.models:
            return 'log_db'
        return None

    def db_for_write(self, model, **hints):
        if str(model._meta) in self.models:
            return 'log_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'swu' or \
           obj2._meta.app_label == 'swu':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == 'log_db':
            if app_label == 'swu':
                return model_name in ['generallog', 'speciallog', 'signallog']
            else:
                return False
        if app_label == 'swu':
            return model_name == 'character'
        return None
