(function () {
    // Private function
    function getColumnsForScaffolding(data, action) {
        if ((typeof data.length !== 'number') || data.length === 0) {
            return [];
        }
        var columns = [];
        for (var propertyName in data[0]) {
            columns.push({ headerText: propertyName, rowText: propertyName, action: action });
        }
        return columns;
    }

    ko.simpleGrid = {
        // Defines a view model class you can use to populate a grid
        viewModel: function (configuration) {
            this.data = ko.observable(configuration.data);
            this.currentPageIndex = ko.observable(0);
            this.pageSize = configuration.pageSize || 5;
            this.action = configuration.action;

            // If you don't specify columns configuration, we'll use scaffolding
            this.columns = configuration.columns || getColumnsForScaffolding(ko.unwrap(this.data), configuration.action);

            this.itemsOnCurrentPage = ko.computed(function () {
                var startIndex = this.pageSize * this.currentPageIndex();
                return ko.unwrap(this.data()).slice(startIndex, startIndex + this.pageSize);
            }, this);

            this.maxPageIndex = ko.computed(function () {
                return Math.ceil(ko.unwrap(this.data).length / this.pageSize) - 1;
            }, this);
        }
    };

    // Templates used to render the grid
    var templateEngine = new ko.nativeTemplateEngine();

    templateEngine.addTemplate = function(templateName, templateMarkup) {
        document.write("<script type='text/html' id='" + templateName + "'>" + templateMarkup + "<" + "/script>");
    };

    templateEngine.addTemplate("ko_simpleGrid_grid", "\
                    <table class=\"ko-grid\" cellspacing=\"0\">\
                        <thead>\
                            <tr data-bind=\"foreach: columns\">\
                               <th data-bind=\"text: headerText\"></th>\
                            </tr>\
                            <tr data-bind=\"foreach: columns\">\
                               <th data-bind=\"if: isFilter, visible:!searchButton\"><input data-bind=\"attr:{id:rowText+ '_filter'}\" type=\"text\" placeholder=\"Escriba aqu&iacute;...\"></th>\
                               <th data-bind=\"if: searchButton, visible: searchButton\"><button class=\"btn btn-primary  btn-group-lg\" id=\"btnBuscarPredios\" type=\"button\" data-bind=\"click: searchButtonAction\" title=\"Buscar\"><i class=\"glyphicon glyphicon-search\"></i></button></th>\
                            </tr>\
                        </thead>\
                        <tbody data-bind=\"foreach: itemsOnCurrentPage\">\
                           <tr data-bind=\"foreach: $parent.columns\">\
                               <td data-bind=\"text: typeof rowText == 'function' ? rowText($parent) : $parent[rowText], click: $root.action ? function(){ $root.action($parent) } : function(){} \"></td>\
                            </tr>\
                        </tbody>\
                    </table>");
    templateEngine.addTemplate("ko_simpleGrid_pageLinks", "\
                    <div class=\"ko-grid-pageLinks\">\
                        <span>P&aacute;gina:</span>\
                        <!-- ko foreach: ko.utils.range(0, maxPageIndex) -->\
                               <a href=\"#\" data-bind=\"text: $data + 1, click: function() { $root.currentPageIndex($data) }, css: { selected: $data == $root.currentPageIndex() }\">\
                            </a>\
                        <!-- /ko -->\
                    </div>");

    // The "simpleGrid" binding
    ko.bindingHandlers.simpleGrid = {
        init: function() {
            return { 'controlsDescendantBindings': true };
        },
        // This method is called to initialize the node, and will also be called again if you change what the grid is bound to
        update: function (element, viewModelAccessor, allBindings) {
            var viewModel = viewModelAccessor();

            // Empty the element
            while(element.firstChild)
                ko.removeNode(element.firstChild);

            // Allow the default templates to be overridden
            var gridTemplateName      = "ko_simpleGrid_grid",
                pageLinksTemplateName = "ko_simpleGrid_pageLinks";

            // Render the main grid
            var gridContainer = element.appendChild(document.createElement("DIV"));
            ko.renderTemplate(gridTemplateName, viewModel, { templateEngine: templateEngine }, gridContainer, "replaceNode");

            // Render the page links
            var pageLinksContainer = element.appendChild(document.createElement("DIV"));
            ko.renderTemplate(pageLinksTemplateName, viewModel, { templateEngine: templateEngine }, pageLinksContainer, "replaceNode");
        }
    };
})();