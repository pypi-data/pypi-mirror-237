import { ChartModel, ChartUtils, ChartTheme } from '@deephaven/chart';
import Log from '@deephaven/log';
import { applyColorwayToData } from './PlotlyExpressChartUtils.js';
const log = Log.module('@deephaven/js-plugin-plotly-express.ChartModel');
export class PlotlyExpressChartModel extends ChartModel {
    constructor(dh, tableColumnReplacementMap, data, plotlyLayout, isDefaultTemplate = true, theme = ChartTheme) {
        var _a, _b, _c, _d, _e, _f, _g, _h, _j, _k, _l;
        super(dh);
        this.tableSubscriptionCleanups = [];
        this.isPaused = false;
        this.hasPendingUpdate = false;
        this.handleFigureUpdated = this.handleFigureUpdated.bind(this);
        this.chartUtils = new ChartUtils(dh);
        this.tableColumnReplacementMap = new Map(tableColumnReplacementMap);
        this.chartDataMap = new Map();
        this.tableSubscriptionMap = new Map();
        this.theme = theme;
        this.data = data;
        const template = { layout: this.chartUtils.makeDefaultLayout(theme) };
        // For now we will only use the plotly theme colorway since most plotly themes are light mode
        if (!isDefaultTemplate) {
            template.layout.colorway =
                (_c = (_b = (_a = plotlyLayout.template) === null || _a === void 0 ? void 0 : _a.layout) === null || _b === void 0 ? void 0 : _b.colorway) !== null && _c !== void 0 ? _c : template.layout.colorway;
        }
        this.plotlyLayout = plotlyLayout;
        this.layout = Object.assign(Object.assign({}, plotlyLayout), { template });
        applyColorwayToData((_g = (_f = (_e = (_d = this.layout) === null || _d === void 0 ? void 0 : _d.template) === null || _e === void 0 ? void 0 : _e.layout) === null || _f === void 0 ? void 0 : _f.colorway) !== null && _g !== void 0 ? _g : [], (_l = (_k = (_j = (_h = this.plotlyLayout) === null || _h === void 0 ? void 0 : _h.template) === null || _j === void 0 ? void 0 : _j.layout) === null || _k === void 0 ? void 0 : _k.colorway) !== null && _l !== void 0 ? _l : [], this.data);
        this.setTitle(this.getDefaultTitle());
    }
    getData() {
        return this.data;
    }
    getLayout() {
        return this.layout;
    }
    subscribe(callback) {
        super.subscribe(callback);
        const { dh } = this;
        this.tableColumnReplacementMap.forEach((_, table) => this.chartDataMap.set(table, new dh.plot.ChartData(table)));
        this.tableColumnReplacementMap.forEach((columnReplacements, table) => {
            const columnNames = new Set(columnReplacements.keys());
            const columns = table.columns.filter(({ name }) => columnNames.has(name));
            this.tableSubscriptionMap.set(table, table.subscribe(columns));
        });
        this.startListening();
    }
    unsubscribe(callback) {
        super.unsubscribe(callback);
        this.stopListening();
        this.tableSubscriptionMap.forEach(sub => sub.close());
        this.chartDataMap.clear();
    }
    handleFigureUpdated(event, chartData, columnReplacements) {
        if (chartData == null || columnReplacements == null) {
            log.warn('Unknown chartData or columnReplacements for this event. Skipping update');
            return;
        }
        const { detail: figureUpdateEvent } = event;
        chartData.update(figureUpdateEvent);
        columnReplacements.forEach((destinations, column) => {
            const columnData = chartData.getColumn(column, val => this.chartUtils.unwrapValue(val), figureUpdateEvent);
            destinations.forEach(destination => {
                // The JSON pointer starts w/ /plotly and we don't need that part
                const parts = destination
                    .split('/')
                    .filter(part => part !== '' && part !== 'plotly');
                // eslint-disable-next-line @typescript-eslint/no-this-alias, @typescript-eslint/no-explicit-any
                let selector = this;
                for (let i = 0; i < parts.length; i += 1) {
                    if (i !== parts.length - 1) {
                        selector = selector[parts[i]];
                    }
                    else {
                        selector[parts[i]] = columnData;
                    }
                }
            });
        });
        const { data } = this;
        if (this.isPaused) {
            this.hasPendingUpdate = true;
            return;
        }
        this.fireUpdate(data);
    }
    startListening() {
        this.tableSubscriptionMap.forEach((sub, table) => {
            this.tableSubscriptionCleanups.push(sub.addEventListener(this.dh.Table.EVENT_UPDATED, e => this.handleFigureUpdated(e, this.chartDataMap.get(table), this.tableColumnReplacementMap.get(table))));
        });
    }
    stopListening() {
        this.tableSubscriptionCleanups.forEach(cleanup => cleanup());
    }
    fireUpdate(data) {
        super.fireUpdate(data);
        this.hasPendingUpdate = false;
    }
    pauseUpdates() {
        this.isPaused = true;
    }
    resumeUpdates() {
        this.isPaused = false;
        if (this.hasPendingUpdate) {
            this.fireUpdate(this.data);
        }
    }
    has3D() {
        return this.data.some(({ type }) => type != null && type.includes('3d'));
    }
    getPlotWidth() {
        var _a, _b, _c, _d;
        if (!this.rect || !this.rect.width) {
            return 0;
        }
        return Math.max(this.rect.width -
            ((_b = (_a = this.layout.margin) === null || _a === void 0 ? void 0 : _a.l) !== null && _b !== void 0 ? _b : 0) -
            ((_d = (_c = this.layout.margin) === null || _c === void 0 ? void 0 : _c.r) !== null && _d !== void 0 ? _d : 0), 0);
    }
    getPlotHeight() {
        var _a, _b, _c, _d;
        if (!this.rect || !this.rect.height) {
            return 0;
        }
        return Math.max(this.rect.height -
            ((_b = (_a = this.layout.margin) === null || _a === void 0 ? void 0 : _a.t) !== null && _b !== void 0 ? _b : 0) -
            ((_d = (_c = this.layout.margin) === null || _c === void 0 ? void 0 : _c.b) !== null && _d !== void 0 ? _d : 0), 0);
    }
}
export default PlotlyExpressChartModel;
//# sourceMappingURL=PlotlyExpressChartModel.js.map