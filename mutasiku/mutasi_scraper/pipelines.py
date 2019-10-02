import hashlib
import datetime

from mutasiku.statements.models import Bank, Statement


"""
Bank
-----
id
name

Statement
--------
tanggal
keterangan
keluar
masuk
hashId
ballance
"""


class IdIbankingPipeline(object):
    def process_item(self, item, spider):
        return item


class IdIbankingHashPipeline(object):
    def process_item(self, item, spider):
        to_hash = "%s;%s;%s;%s" % (
            item["tanggal"],
            item["keterangan"],
            item["keluar"],
            item["masuk"],
        )
        item["hash_id"] = hashlib.md5(to_hash.encode()).hexdigest()
        return item


class IdIbankingParseFloatPipeline(object):
    def process_item(self, item, spider):

        """parse masuk & keluar to be float"""

        def parse_(string):
            return float(string.replace(".", "").replace(",", "."))

        item["masuk"] = parse_(item["masuk"])
        item["keluar"] = parse_(item["keluar"])

        item["ballance"] = spider.last_ballance
        return item


class AddBallancePipeline(object):
    def process_item(self, item, spider):
        spider.last_ballance -= item["keluar"]
        spider.last_ballance += item["masuk"]
        item["ballance"] = spider.last_ballance
        return item


class ParseDatePipeline(object):
    def process_item(self, item, spider):
        item["tanggal"] = datetime.datetime.strptime(item["tanggal"], "%d/%m/%Y")
        return item


class DjangoItemPipeline(object):

    def process_item(self, item, spider):
        bank = Bank.objects.filter(name=spider.name).first()
        if not bank:
            bank = Bank.objects.create(name=spider.name)

        statement = Statement.objects.filter(hash_id=item["hash_id"]).first()

        if not statement:
            Statement.objects.create(
                masuk=item["masuk"],
                keluar=item["keluar"],
                ballance=item["ballance"],
                bank=bank,
                keterangan=item["keterangan"],
                tanggal=item["tanggal"],
                hash_id=item["hash_id"]
            )

        return item
