<script lang="ts">
  import { Router, Route, Link } from "svelte-routing";
  import Home from "./pages/home.svelte";
  import Transactions from "./pages/transactions.svelte";
  import Login from "./pages/login.svelte";

  let logged = true;
</script>

{#if logged}
  <div class="drawer h-screen">
    <Router>
      <input id="page-drawer" type="checkbox" class="drawer-toggle" />
      <div class="drawer-content min-h-screen flex flex-col">
        <!-- Page content here -->
        <main class="flex flex-grow">
          <nav class="flex-none w-14 h-full">
            <label for="page-drawer" class="btn btn-square btn-ghost"
              ><svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                class="inline-block w-5 h-5 stroke-current"
                ><path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M4 6h16M4 12h16M4 18h16"
                /></svg
              >
            </label>
          </nav>
          <div class="flex flex-col p-2 w-full lg:max-h-[700px] overflow-auto">
            <Route path="/"><Home /></Route>
            <Route path="/transactions"><Transactions /></Route>
          </div>
        </main>
        <footer
          class="footer footer-center flex-shrink-0 p-4 bg-base-300 text-base-content"
        >
          <div>
            <p>Copyright © 2023 - All right reserved</p>
          </div>
        </footer>
      </div>
      <nav class="drawer-side">
        <label for="page-drawer" class="drawer-overlay" />
        <ul class="menu p-4 w-60 h-full bg-base-200 text-base-content">
          <!-- Sidebar content here -->
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/transactions">Transactions</Link>
          </li>
          <li>
            <button on:click={() => (logged = false)}>Logout<button /> </button>
          </li>
        </ul>
      </nav>
    </Router>
  </div>
{/if}

{#if !logged}
  <Login />
{/if}
