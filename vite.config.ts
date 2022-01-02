import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'
import sveltePreprocess from 'svelte-preprocess';
import path from 'path';

// https://vitejs.dev/config/
export default defineConfig({
  root: './src',
  publicDir: './static',
  build: {
    outDir: '../dist',
    emptyOutDir: true
  },
  plugins: [
    svelte({
      // Recommendable when mdc-typography is used
      onwarn: (warning, handler) => {
        const { code, frame } = warning;
        if (code === "css-unused-selector")
            return;

        handler(warning);
      },
      preprocess: [
        sveltePreprocess({
          typescript: true
        })
      ]
    })
  ],
  resolve: {
    alias: {
      '@components': path.resolve('./src/lib/components')
    }
  }
})
