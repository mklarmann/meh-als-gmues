# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Depot'
        db.create_table(u'loco_app_depot', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(default='', max_length=1000)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'loco_app', ['Depot'])

        # Adding model 'AboType'
        db.create_table(u'loco_app_abotype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=1000)),
        ))
        db.send_create_signal(u'loco_app', ['AboType'])

        # Adding model 'ExtraAboType'
        db.create_table(u'loco_app_extraabotype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal(u'loco_app', ['ExtraAboType'])

        # Adding model 'Abo'
        db.create_table(u'loco_app_abo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('abotype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['loco_app.AboType'])),
            ('depot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['loco_app.Depot'])),
        ))
        db.send_create_signal(u'loco_app', ['Abo'])

        # Adding M2M table for field users on 'Abo'
        db.create_table(u'loco_app_abo_users', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('abo', models.ForeignKey(orm[u'loco_app.abo'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(u'loco_app_abo_users', ['abo_id', 'user_id'])

        # Adding M2M table for field extra_abos on 'Abo'
        db.create_table(u'loco_app_abo_extra_abos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('abo', models.ForeignKey(orm[u'loco_app.abo'], null=False)),
            ('extraabotype', models.ForeignKey(orm[u'loco_app.extraabotype'], null=False))
        ))
        db.create_unique(u'loco_app_abo_extra_abos', ['abo_id', 'extraabotype_id'])

        # Adding model 'Loco'
        db.create_table(u'loco_app_loco', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name='loco', unique=True, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'loco_app', ['Loco'])


    def backwards(self, orm):
        # Deleting model 'Depot'
        db.delete_table(u'loco_app_depot')

        # Deleting model 'AboType'
        db.delete_table(u'loco_app_abotype')

        # Deleting model 'ExtraAboType'
        db.delete_table(u'loco_app_extraabotype')

        # Deleting model 'Abo'
        db.delete_table(u'loco_app_abo')

        # Removing M2M table for field users on 'Abo'
        db.delete_table('loco_app_abo_users')

        # Removing M2M table for field extra_abos on 'Abo'
        db.delete_table('loco_app_abo_extra_abos')

        # Deleting model 'Loco'
        db.delete_table(u'loco_app_loco')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'loco_app.abo': {
            'Meta': {'object_name': 'Abo'},
            'abotype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['loco_app.AboType']"}),
            'depot': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['loco_app.Depot']"}),
            'extra_abos': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['loco_app.ExtraAboType']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'abos'", 'symmetrical': 'False', 'to': u"orm['auth.User']"})
        },
        u'loco_app.abotype': {
            'Meta': {'object_name': 'AboType'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'loco_app.depot': {
            'Meta': {'object_name': 'Depot'},
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'loco_app.extraabotype': {
            'Meta': {'object_name': 'ExtraAboType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'loco_app.loco': {
            'Meta': {'object_name': 'Loco'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'loco'", 'unique': 'True', 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['loco_app']