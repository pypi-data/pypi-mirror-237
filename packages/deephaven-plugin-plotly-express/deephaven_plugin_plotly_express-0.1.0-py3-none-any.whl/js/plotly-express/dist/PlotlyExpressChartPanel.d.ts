/// <reference types="react" />
import { type ChartPanelProps } from '@deephaven/dashboard-core-plugins';
import { type PlotlyChartWidget } from './PlotlyExpressChartUtils.js';
export interface PlotlyExpressChartPanelProps extends ChartPanelProps {
    fetch(): Promise<PlotlyChartWidget>;
}
declare function PlotlyExpressChartPanel(props: PlotlyExpressChartPanelProps): JSX.Element;
declare namespace PlotlyExpressChartPanel {
    var displayName: string;
}
export default PlotlyExpressChartPanel;
//# sourceMappingURL=PlotlyExpressChartPanel.d.ts.map