from flask import Blueprint
import views

#blueprint
sburls = Blueprint('submission',__name__)

sburls.add_url_rule('/', 'submission', views.submission, methods=['GET','POST'])
sburls.add_url_rule('/rules-abstracts', 'rules-abstracts', views.rules_abstracts)
sburls.add_url_rule('/rules-full-papers', 'rules-abstracts', views.rules_abstracts)
sburls.add_url_rule('/abstracts', 'abstracts', views.abstracts, methods=['GET','POST'])
sburls.add_url_rule('/submit', 'submit', views.submit, methods=['GET','POST'])
sburls.add_url_rule('/download/<abkey>', 'service_download', views.service_download)
sburls.add_url_rule('/bysuject/<subject_id>', 'service_subject', views.service_subject)