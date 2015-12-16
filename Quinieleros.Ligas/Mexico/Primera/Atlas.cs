using System;

namespace Quinieleros.Ligas
{
	public class Atlas:EquipoMexico
	{
		public Atlas ()
		{
			this.Apodos = new System.Collections.Generic.List<string> (){ "Los Zorros", "Los Rojinegros" };
			this.Nombre = "Atlas";
			this.Icon = "";
			this.id = "ATLAS";
		}
	}
}

