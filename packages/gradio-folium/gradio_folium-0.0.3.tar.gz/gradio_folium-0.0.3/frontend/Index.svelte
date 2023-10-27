<script lang="ts">
	import type { Gradio } from "@gradio/utils";
	import { Block, BlockLabel } from "@gradio/atoms";
	import { StatusTracker } from "@gradio/statustracker";
	import {normalise_file} from "@gradio/upload";
	import type {FileData} from "@gradio/upload";
	import type { LoadingStatus } from "@gradio/statustracker";
	import { Empty } from "@gradio/atoms";
	import { Plot as PlotIcon } from "@gradio/icons";


	export let elem_id = "";
	export let elem_classes: string[] = [];
	export let visible = true;
	export let value: FileData;
	export let label: string;
	export let container = true;
	export let scale: number | null = null;
	export let min_width: number | undefined = undefined;
	export let loading_status: LoadingStatus;
	export let root: string;
	export let root_url: string;
	export let height: number | null = null;
	export let gradio: Gradio<{
		change: never;
	}>;

	let new_value: FileData;

	$: label = label ?? "Folium Map"

	async function handle_change() {
		gradio.dispatch("change");
	}

	$: height = height ?? 500;
	$: new_value = {...normalise_file(value, root, root_url)};
	$: new_value, handle_change()

</script>

<Block {visible} {elem_id} {elem_classes} {container} {scale} {min_width}>
	{#if loading_status}
		<StatusTracker
			autoscroll={gradio.autoscroll}
			i18n={gradio.i18n}
			{...loading_status}
		/>
	{/if}
	<BlockLabel show_label={true} Icon={PlotIcon} label={label || "Folium Map"} />
	{#if value}
		<iframe src={new_value.data} title={label} height="{height}px"></iframe>
	{:else}
		<Empty unpadded_box={true} size="large"><PlotIcon /></Empty>
	{/if}

</Block>

<style>

	iframe	 {
		display: flex;
		width: var(--size-full);
	}

</style>
