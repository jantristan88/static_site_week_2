top_template = open('templates/top_template.html').read()
bottom_template = open('templates/bottom_template.html').read()

index = open('content/index.html').read()
index_html = top_template + home + bottom_template
open('index.html', 'w+').write(index_html)

FeatureProject= open('content/FeatureProject.html').read()
FeatureProject_html = top_template + FeatureProject + bottom_template
open('FeatureProject.html', 'w+').write(FeaturedProject_html)

Publication = open('content/Publication.html').read()
Publication_html = top_template + content + bottom_template
open('Publication.html', 'w+').write(Publication_html)