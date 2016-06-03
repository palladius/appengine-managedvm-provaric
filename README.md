# Synopsys

AppId: s~managedvm-provaric
ProjectNumber: 233183858767
Pantheon: https://console.cloud.google.com/code/develop/browse/bg1lFAv6R0X/master/1-hello-world/app.yaml?project=managedvm-provaric

# Code in ruby

On 2016-06-02, since code was not online, I followed the Ruby tutorial and now it'sn in the source code: `https://console.cloud.google.com/code/develop/browse/bg1lFAv6R0X/master/1-hello-world/app.yaml?project=managedvm-provaric`.

gcloud config set project managedvm-provaric \
  && gcloud source repos clone default \
    ~/src/managedvm-provaric/ruby_mvms_quickstart \
  && cd ~/src/managedvm-provaric/ruby_mvms_quickstart/1-hello-world \
  && git checkout master

ho messo il codice in default. Per farlo eseguire vai in hello-world e lo deploy cosi  