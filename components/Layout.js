import Head from 'next/head'

import Menu from '../components/Menu';

export default function Layout({ children }) {
    return (
        <nav>
            <Head>
                <title>Welcome to kreimben.com!</title>
            </Head>
            <Menu />
            <main>
                {children}
            </main>
        </nav>
    )
}