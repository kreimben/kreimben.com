import Head from 'next/head';

import Menu from '../components/Menu';

export default function Home() {
    return (
        <>
            <Head>
                <title>Welcome to Kreimben.com!</title>
            </Head>
            <main>
                <Menu />
                <h1>Hello, World!</h1>
            </main>
        </>
    )
}