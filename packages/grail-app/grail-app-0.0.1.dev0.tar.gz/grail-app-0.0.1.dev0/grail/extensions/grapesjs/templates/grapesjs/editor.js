
editor.Panels.addButton
    ('options',
        [{
            id: 'save-db',
            className: 'fa fa-floppy-o',
            command: 'save-db',
            attributes: { title: 'Save Page' }
        }]
    );


// Running commands from panels
const panels = editor.Panels;
panels.addButton('options', {
    id: 'open-templates',
    className: 'fa fa-folder-o',
    attributes: {
        title: 'Open projects and templates'
    },
    command: 'open-templates', //Open modal 
});
panels.addButton('views', {
    id: 'open-pages',
    className: 'fa fa-file-o',
    attributes: {
        title: 'Take Screenshot'
    },
    command: 'open-pages',
    togglable: false
});
// Add the command
editor.Commands.add
    ('save-db', {
        run: function (editor, sender) {
            sender && sender.set('active'); // turn off the button
            editor.store();
        }
    });
const panelViews = panels.addPanel({
    id: 'views'
});
panelViews.get('buttons').add([{
    attributes: {
        title: 'Open Code'
    },
    className: 'fa fa-file-code-o',
    command: 'open-code',
    togglable: true, //do not close when button is clicked again
    id: 'open-code'
}]);

const components = editor.Components;
const blocks = editor.Blocks;
const cmpId = "htmx-template";
const props = (i) => i;

const idTrait = {
    name: "id",
    label: "Id"
};

const titleTrait = {
    name: "title",
    label: "Title"
};

//TODO make color inputs dynamic
const granimProps = {
    name: "htmx-template",
    opacity1: 1,
    opacity2: 1,
    color1: "#EB3349",
    color2: "#F45C43",
    color3: "#1CD8D2",
    color4: "#93EDC7"
};

const nameTrait = {
    type: "text",
    name: "name",
    label: "name",
    placeholder: "granim"
};

const opacity = ["opacity1", "opacity2"].map((name) => ({
    changeProp: 1,
    type: "number",
    min: 0,
    max: 1,
    step: 0.01,
    placeholder: "0-1",
    name
}));

const colors = ["color1", "color2", "color3", "color4"].map((name) => ({
    changeProp: 1,
    type: "color",
    placeholder: "black",
    name
}));

const traits = [nameTrait, ...opacity, ...colors];

components.addType(cmpId, {
    model: {
        defaults: props({
            ...granimProps,
            tagName: "div",
            icon: "<i class='fa fa-code'></i>",
            resizable: 1,
            droppable: 0,
            traits: [idTrait, titleTrait, ...traits],
            style: {
                padding: "0px",
                width: "100%",
                height: "100%"
            },
            script: `
            const float = (num) => parseFloat(num) || 0;
            const init = () => {
              const granimInstance = new Granim({
                element: '#' + this.id,
                name: "{[ name ]}",
                opacity: [float("{[ opacity1 ]}"), float("{[ opacity2 ]}")],
                states: {
                  "default-state": {
                    gradients: [
                      ["{[ color1 ]}", "{[ color2 ]}"],
                      ["{[ color3 ]}", "{[ color3 ]}"]
                    ]
                  }
                }
              });
            };
            if (!window.Granim) {
              const scr = document.createElement("script");
              scr.src = "{[ granimsrc ]}";
              scr.onload = init;
              document.head.appendChild(scr);
            } else {
              init();
            }`
        }),

        init() {
            const events = traits
                .filter((i) => ["strings"].indexOf(i.name) < 0)
                .map((i) => `change:${i.name}`)
                .join(" ");
            this.on(events, () => this.trigger("change:script"));
        }
    }
});
components.addComponent({ type: cmpId }); 