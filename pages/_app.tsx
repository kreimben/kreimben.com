import '../styles/globals.css'
import '../styles/tailwindcssoutput.css'

import type { AppProps } from 'next/app'

function MyApp({ Component, pageProps }: AppProps) {
    console.log("FUCK!!!");

    return <Component {...pageProps} />
}

export default MyApp