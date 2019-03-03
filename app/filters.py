from app import app
import markdown
from markdown.extensions import Extension
import bleach
from bleach_whitelist import markdown_tags, markdown_attrs


class EscapeHtml(Extension):
    def extendMarkdown(self, md, md_globals):
        del md.preprocessors['html_block']
        del md.inlinePatterns['html']

@app.template_filter('markdown')
def markdown_filter(mdtext):
	return bleach.clean(markdown.markdown(mdtext), markdown_tags, markdown_attrs)


