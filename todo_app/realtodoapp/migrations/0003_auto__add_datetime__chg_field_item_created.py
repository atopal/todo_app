# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DateTime'
        db.create_table('realtodoapp_datetime', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('realtodoapp', ['DateTime'])


        # Renaming column for 'Item.created' to match new field type.
        db.rename_column('realtodoapp_item', 'created', 'created_id')
        # Changing field 'Item.created'
        db.alter_column('realtodoapp_item', 'created_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['realtodoapp.DateTime']))
        # Adding index on 'Item', fields ['created']
        db.create_index('realtodoapp_item', ['created_id'])


    def backwards(self, orm):
        # Removing index on 'Item', fields ['created']
        db.delete_index('realtodoapp_item', ['created_id'])

        # Deleting model 'DateTime'
        db.delete_table('realtodoapp_datetime')


        # Renaming column for 'Item.created' to match new field type.
        db.rename_column('realtodoapp_item', 'created_id', 'created')
        # Changing field 'Item.created'
        db.alter_column('realtodoapp_item', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

    models = {
        'realtodoapp.datetime': {
            'Meta': {'object_name': 'DateTime'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'realtodoapp.item': {
            'Meta': {'object_name': 'Item'},
            'created': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['realtodoapp.DateTime']"}),
            'difficulty': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'done': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['realtodoapp']