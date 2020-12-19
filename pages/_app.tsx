import '../styles/globals.css'
import '../styles/tailwindcssoutput.css'

import * as React from 'react'

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