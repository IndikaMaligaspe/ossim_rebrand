This is python based rebranding application written by securmatic in order install ossim, ossec,snort and proprietory plugins

1. The rebrand_config.py will rebrand the following files

  1. /etc/ossim/menu-cfg
  2. /etc/ossim/menu_network.cfg
  3. /etc/ossim/ossim-setup.conf
  4. /etc/hosts/hostname
  5. /etc/hosts/hosts
  6. /etc/issue
  7. /etc/motd-tail

2. Installation
    Download the distribution package and run python setup.py install

3. Configuration
    All configuration will be in the ossim_rebrand_config.yaml. The following gives an update for each area

    source_file: <source file to change>
    source_file_ext: <source file to change extension>
    source_location: <where is the source file>
    dest_file: <a temp file name to update the replaced key words. Normally this will be the same as source file name>
    dest_file_ext: <temp file extenssion, please use .ctr>
    items_list: <A comma separated list of indexes in the source file that will be checked to replace key words. If there are no indexes please leave a []>
    replace_what: <A comma seperated list of words to replace, default is "AlienVault,alienvault">
    replace_with: <A comma seperated list of words to replace with, default is "Securmatic,securmatic">

    config: # configuration for re-branding which is self explanatory
     debug: on
     log: true
     log_location: \opt\rebrand
     log_name: rebrand_log.log
     format: '%d-%t-%f-%l'
