var __rest = (this && this.__rest) || function (s, e) {
    var t = {};
    for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p) && e.indexOf(p) < 0)
        t[p] = s[p];
    if (s != null && typeof Object.getOwnPropertySymbols === "function")
        for (var i = 0, p = Object.getOwnPropertySymbols(s); i < p.length; i++) {
            if (e.indexOf(p[i]) < 0 && Object.prototype.propertyIsEnumerable.call(s, p[i]))
                t[p[i]] = s[p[i]];
        }
    return t;
};
import { jsx as _jsx } from "react/jsx-runtime";
import { useCallback, useEffect, useRef, useState } from 'react';
import Plotly from 'plotly.js-dist-min';
import { ChartPanel, } from '@deephaven/dashboard-core-plugins';
import { ChartTheme } from '@deephaven/chart';
import { useApi } from '@deephaven/jsapi-bootstrap';
import PlotlyExpressChartModel from './PlotlyExpressChartModel.js';
import { getWidgetData, getDataMappings, } from './PlotlyExpressChartUtils.js';
function PlotlyExpressChartPanel(props) {
    const dh = useApi();
    const { fetch } = props, rest = __rest(props, ["fetch"]);
    const containerRef = useRef(null);
    const [model, setModel] = useState();
    const makeModel = useCallback(async () => {
        var _a;
        const widgetInfo = await fetch();
        const data = getWidgetData(widgetInfo);
        const { plotly, deephaven } = data;
        const isDefaultTemplate = !deephaven.is_user_set_template;
        const tableColumnReplacementMap = await getDataMappings(widgetInfo);
        const m = new PlotlyExpressChartModel(dh, tableColumnReplacementMap, plotly.data, (_a = plotly.layout) !== null && _a !== void 0 ? _a : {}, isDefaultTemplate, ChartTheme);
        setModel(m);
        return m;
    }, [dh, fetch]);
    useEffect(function handle3DTicks() {
        if (!model || !containerRef.current || !model.has3D()) {
            return;
        }
        const container = containerRef.current;
        function handleMouseDown() {
            model === null || model === void 0 ? void 0 : model.pauseUpdates();
            // The once option removes the listener after it is called
            window.addEventListener('mouseup', handleMouseUp, { once: true });
        }
        function handleMouseUp() {
            model === null || model === void 0 ? void 0 : model.resumeUpdates();
        }
        let wheelTimeout = 0;
        function handleWheel() {
            model === null || model === void 0 ? void 0 : model.pauseUpdates();
            window.clearTimeout(wheelTimeout);
            wheelTimeout = window.setTimeout(() => {
                model === null || model === void 0 ? void 0 : model.resumeUpdates();
            }, 300);
        }
        container.addEventListener('mousedown', handleMouseDown);
        container.addEventListener('wheel', handleWheel);
        return () => {
            window.clearTimeout(wheelTimeout);
            window.removeEventListener('mouseup', handleMouseUp);
            container.removeEventListener('mousedown', handleMouseDown);
            container.removeEventListener('wheel', handleWheel);
        };
    }, [model]);
    return (_jsx(ChartPanel
    // eslint-disable-next-line react/jsx-props-no-spreading
    , Object.assign({}, rest, { containerRef: containerRef, makeModel: makeModel, Plotly: Plotly })));
}
PlotlyExpressChartPanel.displayName = 'PlotlyExpressChartPanel';
export default PlotlyExpressChartPanel;
//# sourceMappingURL=PlotlyExpressChartPanel.js.map