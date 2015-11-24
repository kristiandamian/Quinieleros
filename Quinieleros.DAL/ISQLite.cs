using System;
using SQLite.Net;

namespace Quinieleros.DAL
{
    public interface ISQLite
    {
        SQLiteConnection GetConnection();
    }
}
