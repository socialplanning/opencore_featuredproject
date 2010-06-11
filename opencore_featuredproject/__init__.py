from Products.CMFCore.utils import getToolByName
from datetime import datetime
from zope.app.component.hooks import getSite
from opencore.utils import get_config
import os

def feature_project(project_id, description):
    """this stores the project_id in a file """
    feature_dir = get_config("featured_project_dir")
    assert os.path.exists(feature_dir)
    assert os.path.isdir(feature_dir)
    filename = os.path.join(feature_dir, project_id)
    fp = open(filename, 'w')
    fp.write(description)
    fp.close()

def get_featured_projects():
    """get some metadata latest featured project, or None"""
    feature_dir = get_config("featured_project_dir")
    assert os.path.exists(feature_dir)
    assert os.path.isdir(feature_dir)
    projects = os.listdir(feature_dir)
    features = []
    for project in projects:
        if project.startswith('.'): continue
        if project.endswith('~'): continue
        fp = open(os.path.join(feature_dir, project))
        desc = fp.read()
        fp.close()
        features.append({'project_id': project, 'description': desc})
    return features
