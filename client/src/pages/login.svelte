<script lang="ts">
  let login = true;
</script>

<div class="flex justify-center items-center h-screen">
  <div class="bg-base-content p-8 rounded shadow-md w-80 text-white">
    <div class="flex mb-8">
      <button
        on:click={() => (login = true)}
        class="flex-1 bg-neutral py-2 px-4 rounded-l hover:bg-neutral-500 focus:outline-none"
        >Login</button
      >
      <button
        on:click={() => (login = false)}
        class="flex-1 bg-neutral py-2 px-4 rounded-r hover:bg-neutral-500 focus:outline-none"
        >Register</button
      >
    </div>

    {#if login}
      <!-- Login Form -->
      <form id="login-form">
        <div class="mb-4">
          <label class="block mb-2 font-medium" for="login-email">Email</label>
          <input
            id="login-email"
            type="email"
            class="input input-bordered w-full max-w-xs"
            placeholder="Email"
            required
          />
        </div>
        <div class="mb-4">
          <label class="block mb-2 font-medium" for="login-password"
            >Password</label
          >
          <input
            id="login-password"
            type="password"
            class="input input-bordered w-full max-w-xs"
            placeholder="Password"
            required
          />
        </div>
        <button
          class="w-full bg-neutral rounded py-2 px-4 hover:bg-neutral-500 transition duration-200"
          type="submit">Login</button
        >
      </form>
    {:else}
      <!-- Register Form -->
      <form id="register-form">
        <div class="mb-4">
          <label class="block mb-2 font-medium" for="register-name">Name</label>
          <input
            id="register-name"
            type="text"
            class="input input-bordered w-full max-w-xs"
            placeholder="Name"
            required
          />
        </div>
        <div class="mb-4">
          <label class="block mb-2 font-medium" for="register-email"
            >Email</label
          >
          <input
            id="register-email"
            type="email"
            class="input input-bordered w-full max-w-xs"
            placeholder="Email"
            required
          />
        </div>
        <div class="mb-4">
          <label class="block mb-2 font-medium" for="register-password"
            >Password</label
          >
          <input
            id="register-password"
            type="password"
            class="input input-bordered w-full max-w-xs"
            placeholder="Password"
            required
          />
        </div>
        <button
          class="w-full bg-neutral rounded py-2 px-4 hover:bg-neutral-500 transition duration-200"
          type="submit">Register</button
        >
      </form>
    {/if}
  </div>
</div>
