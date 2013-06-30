# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Recipe.blah'
        db.delete_column(u'recipes_recipe', 'blah')

        # Deleting field 'Recipe.something'
        db.delete_column(u'recipes_recipe', 'something')

        # Deleting field 'Recipe.bar'
        db.delete_column(u'recipes_recipe', 'bar')

        # Deleting field 'Recipe.baz'
        db.delete_column(u'recipes_recipe', 'baz')

        # Deleting field 'Recipe.foo'
        db.delete_column(u'recipes_recipe', 'foo')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Recipe.blah'
        raise RuntimeError("Cannot reverse this migration. 'Recipe.blah' and its values cannot be restored.")
        # Adding field 'Recipe.something'
        db.add_column(u'recipes_recipe', 'something',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Recipe.bar'
        raise RuntimeError("Cannot reverse this migration. 'Recipe.bar' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Recipe.baz'
        raise RuntimeError("Cannot reverse this migration. 'Recipe.baz' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Recipe.foo'
        raise RuntimeError("Cannot reverse this migration. 'Recipe.foo' and its values cannot be restored.")

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
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipes.Category']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'ingredients': ('django.db.models.fields.TextField', [], {}),
            'instructions': ('django.db.models.fields.TextField', [], {}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['recipes']