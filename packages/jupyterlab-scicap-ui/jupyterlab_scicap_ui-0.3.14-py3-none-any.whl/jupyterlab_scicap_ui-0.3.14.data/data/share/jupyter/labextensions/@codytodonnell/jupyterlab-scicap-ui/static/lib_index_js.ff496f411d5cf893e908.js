"use strict";
(self["webpackChunk_codytodonnell_jupyterlab_scicap_ui"] = self["webpackChunk_codytodonnell_jupyterlab_scicap_ui"] || []).push([["lib_index_js"],{

/***/ "./lib/handler.js":
/*!************************!*\
  !*** ./lib/handler.js ***!
  \************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   requestAPI: () => (/* binding */ requestAPI)
/* harmony export */ });
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/services */ "webpack/sharing/consume/default/@jupyterlab/services");
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__);


/**
 * Call the API extension
 *
 * @param endPoint API REST end point for the extension
 * @param init Initial values for the request
 * @returns The response body interpreted as JSON
 */
async function requestAPI(endPoint = '', init = {}) {
    // Make request to Jupyter API
    const settings = _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.makeSettings();
    const requestUrl = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__.URLExt.join(settings.baseUrl, '@codytodonnell/jupyterlab-scicap-ui', // API Namespace
    endPoint);
    let response;
    try {
        response = await _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.makeRequest(requestUrl, init, settings);
    }
    catch (error) {
        throw new _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.NetworkError(error);
    }
    let data = await response.text();
    if (data.length > 0) {
        try {
            data = JSON.parse(data);
        }
        catch (error) {
            console.log('Not a JSON response body.', response);
        }
    }
    if (!response.ok) {
        throw new _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.ResponseError(response, data.message || data);
    }
    return data;
}


/***/ }),

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/launcher */ "webpack/sharing/consume/default/@jupyterlab/launcher");
/* harmony import */ var _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _widget__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./widget */ "./lib/widget.js");
/* harmony import */ var _handler__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./handler */ "./lib/handler.js");
/* harmony import */ var _sc_service__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./sc-service */ "./lib/sc-service.js");






/**
 * The command IDs used by the react-widget plugin.
 */
var CommandIDs;
(function (CommandIDs) {
    CommandIDs.create = 'create-react-widget';
})(CommandIDs || (CommandIDs = {}));
/**
 * Initialization data for the react-widget extension.
 */
const extension = {
    id: 'react-widget',
    autoStart: true,
    optional: [_jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_1__.ILauncher],
    activate: (app, launcher) => {
        (0,_handler__WEBPACK_IMPORTED_MODULE_3__.requestAPI)('sc_api_url')
            .then(result => {
            console.log(result);
            _sc_service__WEBPACK_IMPORTED_MODULE_4__.scService.apiUrl = result.data.apiUrl;
            _sc_service__WEBPACK_IMPORTED_MODULE_4__.scService.apiUrlWindows = result.data.apiUrlWindows;
            console.log(_sc_service__WEBPACK_IMPORTED_MODULE_4__.scService);
        })
            .catch(reason => {
            console.error(`The jupyterlab_scicap_ui server extension appears to be missing.\n${reason}`);
        });
        const { commands } = app;
        const command = CommandIDs.create;
        commands.addCommand(command, {
            caption: 'Open Science Capsule',
            label: 'Science Capsule',
            icon: (args) => (args['isPalette'] ? null : _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__.reactIcon),
            execute: () => {
                const content = new _widget__WEBPACK_IMPORTED_MODULE_5__.ScienceCapsuleWidget();
                const widget = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.MainAreaWidget({ content });
                widget.title.label = 'Science Capsule';
                widget.title.icon = _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__.reactIcon;
                app.shell.add(widget, 'main');
            },
        });
        if (launcher) {
            launcher.add({
                command,
            });
        }
    },
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (extension);


/***/ }),

/***/ "./lib/sc-service.js":
/*!***************************!*\
  !*** ./lib/sc-service.js ***!
  \***************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   scService: () => (/* binding */ scService)
/* harmony export */ });
/**
 * Service to maintain the apiUrl state which is
 * requested asynchronously on start and subsequently
 * used by in the sc-client functions.
 */
const scService = {
    apiUrl: null,
    apiUrlWindows: null
};


/***/ }),

/***/ "./lib/widget.js":
/*!***********************!*\
  !*** ./lib/widget.js ***!
  \***********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   ScienceCapsuleWidget: () => (/* binding */ ScienceCapsuleWidget)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _codytodonnell_scicap_ui__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @codytodonnell/scicap-ui */ "webpack/sharing/consume/default/@codytodonnell/scicap-ui/@codytodonnell/scicap-ui");
/* harmony import */ var _codytodonnell_scicap_ui__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_codytodonnell_scicap_ui__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _sc_service__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./sc-service */ "./lib/sc-service.js");




/**
 * A widget that wraps and renders the Science Capsule UI App
 */
class ScienceCapsuleWidget extends _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.ReactWidget {
    constructor() {
        super();
        this.addClass('jp-ReactWidget');
    }
    render() {
        return react__WEBPACK_IMPORTED_MODULE_2___default().createElement(_codytodonnell_scicap_ui__WEBPACK_IMPORTED_MODULE_1__.App, { apiUrl: _sc_service__WEBPACK_IMPORTED_MODULE_3__.scService.apiUrl, apiUrlWindows: _sc_service__WEBPACK_IMPORTED_MODULE_3__.scService.apiUrlWindows });
    }
}


/***/ })

}]);
//# sourceMappingURL=lib_index_js.ff496f411d5cf893e908.js.map