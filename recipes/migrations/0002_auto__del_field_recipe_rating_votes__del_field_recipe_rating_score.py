# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Recipe.rating_votes'
        db.delete_column(u'recipes_recipe', 'rating_votes')

        # Deleting field 'Recipe.rating_score'
        db.delete_column(u'recipes_recipe', 'rating_score')


    def backwards(self, orm):
        # Adding field 'Recipe.rating_votes'
        db.add_column(u'recipes_recipe', 'rating_votes',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'Recipe.rating_score'
        db.add_column(u'recipes_recipe', 'rating_score',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)


    models = {
        u'recipes.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        },
        u'recipes.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'added_by': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'bar': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'baz': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'blah': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipes.Category']", 'null': 'True', 'blank': 'True'}),
            'foo': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'ingredients': ('django.db.models.fields.TextField', [], {}),
            'instructions': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'something': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['recipes']