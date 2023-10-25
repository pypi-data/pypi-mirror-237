import { ABCWidgetFactory } from '@jupyterlab/docregistry';
import { BlocklyEditor, BlocklyPanel } from './widget';
import { BlocklyRegistry } from './registry';
import { BlocklyManager } from './manager';
import { nullTranslator } from '@jupyterlab/translation';
/**/
var CommandIDs;
(function (CommandIDs) {
    CommandIDs.copyToClipboard = 'blockly:copy-to-clipboard';
})(CommandIDs || (CommandIDs = {}));
/**/
/**
 * A widget factory to create new instances of BlocklyEditor.
 */
export class BlocklyEditorFactory extends ABCWidgetFactory {
    /**
     * Constructor of BlocklyEditorFactory.
     *
     * @param options Constructor options
     */
    constructor(app, options) {
        super(options);
        this._app = app;
        this._registry = new BlocklyRegistry();
        this._rendermime = options.rendermime;
        this._mimetypeService = options.mimetypeService;
        this._trans = (options.translator || nullTranslator).load('jupyterlab');
        //
        app.commands.addCommand(CommandIDs.copyToClipboard, {
            label: this._trans.__('Copy Blockly Output to Clipboard'),
            execute: args => {
                const outputAreaAreas = this._cell.outputArea.node.getElementsByClassName('jp-OutputArea-output');
                if (outputAreaAreas.length > 0) {
                    let element = outputAreaAreas[0];
                    for (let i = 1; i < outputAreaAreas.length; i++) {
                        element.appendChild(outputAreaAreas[i]);
                    }
                    copyElement(element);
                }
            }
        });
        app.contextMenu.addItem({
            command: CommandIDs.copyToClipboard,
            selector: '.jp-OutputArea-child',
            rank: 0
        });
        //
        function copyElement(e) {
            const sel = window.getSelection();
            if (sel == null)
                return;
            // Save the current selection.
            const savedRanges = [];
            for (let i = 0; i < sel.rangeCount; ++i) {
                savedRanges[i] = sel.getRangeAt(i).cloneRange();
            }
            //
            const range = document.createRange();
            range.selectNodeContents(e);
            sel.removeAllRanges();
            sel.addRange(range);
            document.execCommand('copy');
            // Restore the saved selection.
            sel.removeAllRanges();
            savedRanges.forEach(r => sel.addRange(r));
        }
    }
    get registry() {
        return this._registry;
    }
    get manager() {
        return this._manager;
    }
    /**
     * Create a new widget given a context.
     *
     * @param context Contains the information of the file
     * @returns The widget
     */
    createNewWidget(context) {
        // Set a map to the model. The widgets manager expects a Notebook model
        // but the only notebook property it uses is the metadata.
        context.model['metadata'] = new Map();
        const manager = new BlocklyManager(this._app, this._registry, context.sessionContext, this._mimetypeService);
        this._manager = manager;
        const content = new BlocklyPanel(context, manager, this._rendermime);
        //
        this._cell = content.activeLayout.cell;
        return new BlocklyEditor(this._app, { context, content, manager });
    }
}
//# sourceMappingURL=factory.js.map