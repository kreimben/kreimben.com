import '../styles/globals.css'
import '../styles/tailwindcssoutput.css'

import type { AppProps } from 'next/app'

function MyApp({ Component, pageProps }: AppProps) {
    return (
        <>
            <div>Normal state</div>
            <Component {...pageProps} />
        </>
    )
}

export default MyApp