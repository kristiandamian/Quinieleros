using System;

namespace Quinieleros.Ligas
{
	public class Celaya:EquipoMexico
	{
		public Celaya ()
		{
			this.Apodos = new System.Collections.Generic.List<string> (){ "Los cajeteros", "Los toros"};
			this.Nombre = "Celaya";
			this.Icon = "";
			this.id = "CELAYA";
		}
	}
}

