import type { Data, PlotlyDataLayoutConfig } from 'plotly.js';
import type { Table } from '@deephaven/jsapi-types';
export interface PlotlyChartWidget {
    getDataAsBase64(): string;
    exportedObjects: {
        fetch(): Promise<Table>;
    }[];
    addEventListener(type: string, fn: (event: CustomEvent<PlotlyChartWidget>) => () => void): void;
}
export interface PlotlyChartWidgetData {
    deephaven: {
        mappings: Array<{
            table: number;
            data_columns: Record<string, string[]>;
        }>;
        is_user_set_template: boolean;
        is_user_set_color: boolean;
    };
    plotly: PlotlyDataLayoutConfig;
}
export declare function getWidgetData(widgetInfo: PlotlyChartWidget): PlotlyChartWidgetData;
export declare function getDataMappings(widgetInfo: PlotlyChartWidget): Promise<Map<Table, Map<string, string[]>>>;
/**
 * Applies the colorway to the data unless the data color is not its default value
 * Data color is not default if the user set the color specifically or the plot type sets it
 *
 * @param colorway The colorway from the web UI
 * @param plotlyColorway The colorway from plotly
 * @param data The data to apply the colorway to. This will be mutated
 */
export declare function applyColorwayToData(colorway: string[], plotlyColorway: string[], data: Data[]): void;
//# sourceMappingURL=PlotlyExpressChartUtils.d.ts.map