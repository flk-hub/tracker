<script lang="ts">
  import { Router, Route } from "svelte-routing";
  import Home from "./components/home/home.svelte";
</script>

<div class="flex h-screen">
  <div class="bg-gray-800 text-white w-64 flex flex-col">
    <div class="flex items-center justify-between px-6 py-4">
      <h1 class="text-xl font-semibold">Dashboard</h1>
      <button class="text-gray-500 focus:outline-none focus:text-gray-300">
        <svg
          class="h-6 w-6"
          fill="none"
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path d="M4 6h16M4 12h8m-8 6h16" />
        </svg>
      </button>
    </div>

    <nav class="flex-grow">
      <ul class="space-y-1 px-2 py-3">
        <li class="px-4 py-2 hover:bg-gray-700">
          <a href="#" class="flex items-center space-x-2">
            <svg
              class="h-5 w-5"
              fill="none"
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path d="M12 20h9" />
              <path d="M12 4v16m-7-8l7-8 7 8" />
            </svg>
            <span>Home</span>
          </a>
        </li>
        <li class="px-4 py-2 hover:bg-gray-700">
          <a href="#" class="flex items-center space-x-2">
            <svg
              class="h-5 w-5"
              fill="none"
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path d="M12 20h9" />
              <path d="M12 4v16m-7-8l7-8 7 8" />
            </svg>
            <span>Dashboard</span>
          </a>
        </li>
        <li class="px-4 py-2 hover:bg-gray-700">
          <a href="#" class="flex items-center space-x-2">
            <svg
              class="h-5 w-5"
              fill="none"
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path d="M12 20h9" />
              <path d="M12 4v16m-7-8l7-8 7 8" />
            </svg>
            <span>Analytics</span>
          </a>
        </li>
        <li class="px-4 py-2 hover:bg-gray-700">
          <a href="#" class="flex items-center space-x-2">
            <svg
              class="h-5 w-5"
              fill="none"
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path d="M12 20h9" />
              <path d="M12 4v16m-7-8l7-8 7 8" />
            </svg>
            <span>Settings</span>
          </a>
        </li>
      </ul>
    </nav>
  </div>
  <div class="flex-grow bg-gray-100 p-8">
    <Router>
      <Route component={Home} />
    </Router>
  </div>
</div>
