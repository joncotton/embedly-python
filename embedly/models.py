from UserDict import IterableUserDict


class Url(IterableUserDict, object):

    def __init__(self, data=None, method=None, original_url=None):
        super(Url, self).__init__(data)
        self.method = method or 'url'
        self.original_url = original_url

    def __str__(self):
        return self.__unicode__().encode("utf-8")

    def __unicode__(self):
        r = u'<%s ' % self.method.title()

        if self.original_url:
            r += self.original_url

        r += ' >'
        return r
