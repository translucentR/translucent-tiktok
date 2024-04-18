const { contextBridge, ipcRenderer } = require("electron");

// Electron Store
const Store = require("electron-store");

// Initialize theme store
const themeStore = new Store({
	name: "theme",
	defaults: {
		theme: "dark"
	}
});

// Theme mode toggle API
// theme.set(theme mode: "dark", "light", "system")
contextBridge.exposeInMainWorld('theme', {
    set: (newTheme) => {
        ipcRenderer.invoke("theme-toggle", newTheme);
        themeStore.set("theme", newTheme);
    },
    get: () => {
        return themeStore.get("theme");
    }
});

contextBridge.exposeInMainWorld('electronAPI', {
    toggleMaximize: () => ipcRenderer.invoke("window/toggle-max"),
    minimize: () => ipcRenderer.invoke("window/minimize"),
    close: () => ipcRenderer.invoke("window/close"),
    getWindowState: () => ipcRenderer.invoke("window/get-state"),
    selectDirectory: () => ipcRenderer.invoke("window/select-directory")
});