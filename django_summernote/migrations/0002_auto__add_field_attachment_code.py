# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Attachment.code'
        db.add_column(u'django_summernote_attachment', 'code',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=10),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Attachment.code'
        db.delete_column(u'django_summernote_attachment', 'code')


    models = {
        u'django_summernote.attachment': {
            'Meta': {'object_name': 'Attachment'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'uploaded': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['django_summernote']