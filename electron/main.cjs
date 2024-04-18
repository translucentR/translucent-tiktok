const windowStateManager = require("electron-window-state");
const contextMenu = require("electron-context-menu");
const { app, BrowserWindow, ipcMain, nativeTheme, dialog } = require("electron");
const serve = require("electron-serve");
const Store = require("electron-store");
const path = require('path');
const { spawn } = require('child_process'); // Import spawn

// Initialize electron-store
Store.initRenderer();

const serveURL = serve({ directory: "." });
const port = process.env.PORT || 3000;
const dev = !app.isPackaged;

// Keep a global reference of the window object
let mainWindow;

function createWindow() {
    let windowState = windowStateManager({
        defaultHeight: 700,
        defaultWidth: 1000
    });

    mainWindow = new BrowserWindow({
        backgroundColor: "#192127",
        frame: false,
        minHeight: 600,
        minWidth: 800,
        webPreferences: {
            contextIsolation: true,
            devTools: dev,
            nodeIntegration: true,
            preload: path.join(__dirname, 'preload.cjs')
        },
        x: windowState.x,
        y: windowState.y,
        width: windowState.width,
        height: windowState.height,
        show: false
    });

    windowState.manage(mainWindow);

    if (dev) {
        mainWindow.openDevTools();
        mainWindow.setIcon('./static/icon.ico');
        mainWindow.loadURL(`http://localhost:${port}`);
        
        // Spawn Python backend when in development mode
        spawn('python', ['./backend/app.py'], { stdio: 'inherit' });
    }

    process.env['ELECTRON_DISABLE_SECURITY_WARNINGS'] = true;
    
    mainWindow.on('closed', () => {
        mainWindow = null;
    });

    mainWindow.once('ready-to-show', () => {
        mainWindow.show();
    });
}

contextMenu({
    showLookUpSelection: false,
    showSearchWithGoogle: false,
    showCopyImage: false,
    prepend: (defaultActions, params, browserWindow) => [{
        label: "Custom item",
    }],
});

const gotTheLock = app.requestSingleInstanceLock();

if (!gotTheLock) {
    app.quit();
} else {
    app.on('second-instance', () => {
        if (mainWindow) {
            if (mainWindow.isMinimized()) mainWindow.restore();
            mainWindow.focus();
        }
    });
    app.whenReady().then(createWindow);
}

app.on('ready', createWindow);
app.on('activate', () => {
    if (mainWindow === null) createWindow();
});
app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') app.quit();
});

ipcMain.handle("theme-toggle", (e, theme) => {
    nativeTheme.themeSource = theme;
});
ipcMain.handle("window/get-state", () => {
    return mainWindow.isMaximized();
});
ipcMain.handle("window/toggle-max", () => {
    if (mainWindow.isMaximized()) { return mainWindow.restore() }
    mainWindow.maximize();
});
ipcMain.handle("window/minimize", () => {
    mainWindow.minimize();
});
ipcMain.handle("window/close", () => {
    mainWindow.close();
});
ipcMain.handle("window/select-directory", async () => {
    const { canceled, filePaths } = await dialog.showOpenDialog(mainWindow, {
        properties: ['openDirectory']
    });

    if (canceled) {
        return ''; // No selection was made
    } else {
        return filePaths[0]; // Return the first selected path
    }
});
