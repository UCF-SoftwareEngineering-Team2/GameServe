# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Sport'
        db.create_table(u'events_sport', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sportType', self.gf('django.db.models.fields.CharField')(unique=True, max_length=10)),
        ))
        db.send_create_signal(u'events', ['Sport'])

        # Adding model 'Court'
        db.create_table(u'events_court', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sport', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sport', to=orm['events.Sport'])),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'events', ['Court'])

        # Adding model 'Event'
        db.create_table(u'events_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dateTime', self.gf('django.db.models.fields.DateTimeField')()),
            ('endTime', self.gf('django.db.models.fields.DateTimeField')()),
            ('duration', self.gf('django.db.models.fields.FloatField')()),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='creator', to=orm['profile.User'])),
            ('court', self.gf('django.db.models.fields.related.ForeignKey')(related_name='court', to=orm['events.Court'])),
        ))
        db.send_create_signal(u'events', ['Event'])

        # Adding M2M table for field participants on 'Event'
        m2m_table_name = db.shorten_name(u'events_event_participants')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm[u'events.event'], null=False)),
            ('user', models.ForeignKey(orm[u'profile.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'user_id'])

        # Adding M2M table for field checkedInParticipants on 'Event'
        m2m_table_name = db.shorten_name(u'events_event_checkedInParticipants')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm[u'events.event'], null=False)),
            ('user', models.ForeignKey(orm[u'profile.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'user_id'])

        # Adding model 'RecentActivity'
        db.create_table(u'events_recentactivity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Event'])),
            ('activity', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'events', ['RecentActivity'])


    def backwards(self, orm):
        # Deleting model 'Sport'
        db.delete_table(u'events_sport')

        # Deleting model 'Court'
        db.delete_table(u'events_court')

        # Deleting model 'Event'
        db.delete_table(u'events_event')

        # Removing M2M table for field participants on 'Event'
        db.delete_table(db.shorten_name(u'events_event_participants'))

        # Removing M2M table for field checkedInParticipants on 'Event'
        db.delete_table(db.shorten_name(u'events_event_checkedInParticipants'))

        # Deleting model 'RecentActivity'
        db.delete_table(u'events_recentactivity')


    models = {
        u'events.court': {
            'Meta': {'ordering': "('sport',)", 'object_name': 'Court'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'sport': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sport'", 'to': u"orm['events.Sport']"})
        },
        u'events.event': {
            'Meta': {'ordering': "('dateTime',)", 'object_name': 'Event'},
            'checkedInParticipants': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'checkedInParticipants'", 'symmetrical': 'False', 'to': u"orm['profile.User']"}),
            'court': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'court'", 'to': u"orm['events.Court']"}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'creator'", 'to': u"orm['profile.User']"}),
            'dateTime': ('django.db.models.fields.DateTimeField', [], {}),
            'duration': ('django.db.models.fields.FloatField', [], {}),
            'endTime': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participants': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'participants'", 'symmetrical': 'False', 'to': u"orm['profile.User']"})
        },
        u'events.recentactivity': {
            'Meta': {'ordering': "('id',)", 'object_name': 'RecentActivity'},
            'activity': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'events.sport': {
            'Meta': {'object_name': 'Sport'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sportType': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'})
        },
        u'profile.user': {
            'Meta': {'object_name': 'User', 'db_table': "'usertable'"},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'reputation': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        }
    }

    complete_apps = ['events']