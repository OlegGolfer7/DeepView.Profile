'use babel';

import React from 'react';
import ReactDOM from 'react-dom';

import PerfVis from './components/PerfVis';
import Connection from './io/connection';
import MessageHandler from './io/message_handler';
import MessageSender from './io/message_sender';
import Protocol from './io/protocol';
import AppState from './models/AppState';
import PerfVisState from './models/PerfVisState';
import INNPVStore from './stores/innpv_store';
import BatchSizeStore from './stores/batchsize_store';
import OperationInfoStore from './stores/operationinfo_store';
import { getTextEditor } from './utils';

export default class PerfvisPlugin {
  constructor() {
    this._contentsChanged = this._contentsChanged.bind(this);
    this._handleMessage = this._handleMessage.bind(this);
    this._requestAnalysis = this._requestAnalysis.bind(this);
    this._getStartedClicked = this._getStartedClicked.bind(this);
  }

  open() {
    if (INNPVStore.getAppState() !== AppState.ACTIVATED) {
      return;
    }
    INNPVStore.setAppState(AppState.OPENED);

    this._panel = atom.workspace.addRightPanel({item: document.createElement('div')});
    ReactDOM.render(
      <PerfVis handleGetStartedClick={this._getStartedClicked} />,
      this._panel.getItem(),
    );

    this._connection = new Connection(this._handleMessage);
    this._protocol = new Protocol();
    this._messageSender = new MessageSender(this._connection, this._protocol);
    this._messageHandler = new MessageHandler(
      this._messageSender, this._protocol);
  }

  close() {
    if (INNPVStore.getAppState() === AppState.ACTIVATED) {
      return;
    }
    INNPVStore.setAppState(AppState.ACTIVATED);
    INNPVStore.ignoreEditorChanges();

    if (this._editorDebounce != null) {
      clearTimeout(this._editorDebounce);
      this._editorDebounce = null;
    }
    this._connection.close();
    this._connection = null;
    this._messageHandler = null;
    this._messageSender = null;
    this._editor = null;

    ReactDOM.unmountComponentAtNode(this._panel.getItem());
    this._panel.destroy();
    this._panel = null;

    INNPVStore.reset();
    BatchSizeStore.reset();
    OperationInfoStore.reset();
  }

  _getStartedClicked(event) {
    if (INNPVStore.getAppState() !== AppState.OPENED) {
      return;
    }

    INNPVStore.setAppState(AppState.CONNECTING);
    Promise.all([getTextEditor(), this._connection.connect('localhost', 6060)]).then((values) => {
      this._editor = values[0];
      INNPVStore.setEditor(this._editor, this._contentsChanged);
      INNPVStore.subscribeToEditorChanges();

      INNPVStore.setAppState(AppState.CONNECTED);
      console.log('Connected!');
      this._requestAnalysis();
    });
  }

  _contentsChanged(event) {
    if (this._editorDebounce != null) {
      clearTimeout(this._editorDebounce);
    }
    this._editorDebounce = setTimeout(this._requestAnalysis, 1000);
    INNPVStore.setPerfVisState(PerfVisState.DEBOUNCING);
  }

  _handleMessage(message) {
    this._messageHandler.handleMessage(message);
  }

  _requestAnalysis() {
    console.log('Sending analysis request...');
    INNPVStore.setPerfVisState(PerfVisState.ANALYZING);
    this._messageSender.sendAnalyzeRequest(this._editor.getBuffer().getText());
  }
}
