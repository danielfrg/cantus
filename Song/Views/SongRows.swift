//
//  SongRows.swift
//  Cantus
//
//  Created by Daniel Rodriguez on 4/5/21.
//

import SwiftUI

struct SongRow: View {
    var song: Song
    
    var body: some View {
        HStack {
            Text(song.name)
            Spacer()
        }
    }
}

struct SongRows_Previews: PreviewProvider {
    static var previews: some View {
        SongRow(song: songs[0])
    }
}
