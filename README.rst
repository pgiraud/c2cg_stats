stats README
==================

Getting Started
---------------

- cd <directory containing this file>

- $venv/bin/python setup.py develop

- $venv/bin/initialize_stats_db development.ini

- $venv/bin/pserve development.ini

Adding to Your Application
--------------------------

Add the following javascript code to viewer.js:

    var tools = {};
    var toolbar = GeoExt.MapPanel.guess().ownerCt.getTopToolbar();
    toolbar.items.each(function(tool) {
        tool.on('click', function(){
            var id = tool.iconCls;
            if (!tools[id]) {
                tools[id] = 1;
            } else {
                tools[id]++;
            }
        });
    });
    window.onunload = function() {
        Ext.Ajax.request({
            url: '/stats',
            method: 'GET',
            params: tools
        });
    };
