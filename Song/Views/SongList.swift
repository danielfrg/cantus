//
//  SongList.swift
//  Cantus
//
//  Created by Daniel Rodriguez on 4/5/21.
//

import SwiftUI

struct SongList: View {
    var body: some View {
        NavigationView {
            List(songs) { song in
                NavigationLink(destination: SongDetail(song: song)) {
                    SongRow(song: song)
                }
            }
            .navigationTitle("Songs")
        }
    }
}

struct SongList_Previews: PreviewProvider {
    static var previews: some View {
        SongList()
    }
}
