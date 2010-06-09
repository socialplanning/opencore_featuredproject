from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from opencore.browser.base import BaseView
from opencore_featuredproject import feature_project
from opencore_featuredproject import get_featured_project_metadata

class FeatureProjectView(BaseView):
    """handle posting to feature a new project"""

    def respond(self):
        portal_url = getToolByName(self.context, 'portal_url')()
        self.redirect(portal_url + '/projects')

    def process(self):
        if self.request.environ['REQUEST_METHOD'] != 'POST':
            return

        portal_url = getToolByName(self.context, 'portal_url')()

        project_id = self.request.form.get('project_id', None)
        if project_id is None:
            return self.respond()

        portal = getToolByName(
            self.context, 'portal_url').getPortalObject()
        try:
            project = portal['projects'][project_id]
        except KeyError:
            return self.respond()

        desc = self.request.form.get('description', '')
        if desc == '':
            desc = project.Description()

        feature_project(project_id, desc)

        self.add_status_message(u'Project <a href="%s">%s</a> featured' %
                                (portal_url + '/projects/' + project_id,
                                 project_id))
        return self.respond()

class LatestFeaturedProjectView(BrowserView):
    """handle querying for the latest featured project"""

    def get_project(self, project_id):
        portal = getToolByName(
            self.context, 'portal_url').getPortalObject()
        try:
            project = portal['projects'][project_id]
        except KeyError:
            return None
        
    def featured_projects(self, num=5):
        data = get_featured_project_metadata()
        return data[:num]
