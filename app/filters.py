from app import app
import markdown
from markdown.extensions import Extension
import bleach
from bleach_whitelist import markdown_tags, markdown_attrs

@app.template_filter('markdown')
def markdown_filter(mdtext):
	return bleach.clean(markdown.markdown(mdtext), markdown_tags, markdown_attrs)


