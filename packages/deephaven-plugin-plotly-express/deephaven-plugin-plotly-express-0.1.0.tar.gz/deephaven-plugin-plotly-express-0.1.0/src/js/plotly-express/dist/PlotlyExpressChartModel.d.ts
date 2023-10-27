import type { Layout, Data } from 'plotly.js';
import type { dh as DhType, ChartData, Table, TableSubscription } from '@deephaven/jsapi-types';
import { ChartModel, ChartUtils, ChartTheme } from '@deephaven/chart';
export declare class PlotlyExpressChartModel extends ChartModel {
    constructor(dh: DhType, tableColumnReplacementMap: ReadonlyMap<Table, Map<string, string[]>>, data: Data[], plotlyLayout: Partial<Layout>, isDefaultTemplate?: boolean, theme?: typeof ChartTheme);
    chartUtils: ChartUtils;
    tableSubscriptionMap: Map<Table, TableSubscription>;
    tableSubscriptionCleanups: (() => void)[];
    tableColumnReplacementMap: Map<Table, Map<string, string[]>>;
    chartDataMap: Map<Table, ChartData>;
    theme: typeof ChartTheme;
    data: Data[];
    layout: Partial<Layout>;
    plotlyLayout: Partial<Layout>;
    isPaused: boolean;
    hasPendingUpdate: boolean;
    getData(): Partial<Data>[];
    getLayout(): Partial<Layout>;
    subscribe(callback: (event: CustomEvent) => void): void;
    unsubscribe(callback: (event: CustomEvent) => void): void;
    handleFigureUpdated(event: CustomEvent, chartData: ChartData | undefined, columnReplacements: Map<string, string[]> | undefined): void;
    startListening(): void;
    stopListening(): void;
    fireUpdate(data: unknown): void;
    pauseUpdates(): void;
    resumeUpdates(): void;
    has3D(): boolean;
    getPlotWidth(): number;
    getPlotHeight(): number;
}
export default PlotlyExpressChartModel;
//# sourceMappingURL=PlotlyExpressChartModel.d.ts.map