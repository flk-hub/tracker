<script lang="ts">
  import Graph from "../components/home/graph.svelte";

  let user = "ikl";
</script>

<h1 class="text-2xl font-semibold mb-4">Welcome, {user}</h1>
<p>This is the main content area of the dashboard.</p>
<Graph />
