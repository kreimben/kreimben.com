import Head from 'next/head'

import Menu from '../components/Menu';

export default function Layout( { children } ) {
    return (
        <div>
            <Head>
                <title>Welcome to kreimben.com!</title>
            </Head>
            <Menu />
            { children }
        </div>
    )
}